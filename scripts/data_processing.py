import pandas as pd
from prophet import Prophet


def load_data(filepath="data/owid-energy-data.csv", melt=True):
    df = pd.read_csv(filepath)
    df = df[(df["iso_code"].str.len() == 3) | (df["country"] == "World")]
    
    # Columnas de generación de electricidad
    electricity_cols = [col for col in df.columns if col.endswith("_electricity") and not col.endswith("per_capita_electricity")]
    df_energy_sources = df[["country", "iso_code", "year"] + electricity_cols].copy()
    df_demand = df[["country", "iso_code", "year", "electricity_generation", "electricity_demand", "carbon_intensity_elec", "renewables_share_elec", "fossil_share_elec", "electricity_demand_per_capita"]].copy()
    
    # Filtrar desde el año 2000 para la generación vs. demanda
    df_demand = df_demand[df_demand["year"] >= 2000]
    
    # Calcular nuevas métricas
    df_demand["efficiency"] = df_demand["electricity_generation"] / df_demand["electricity_demand"]
    df_demand.sort_values(by=["country", "year"], inplace=True)
    df_demand["generation_growth"] = df_demand.groupby("country")["electricity_generation"].pct_change() * 100
    
    if melt:
        df_energy_sources = df_energy_sources.melt(
            id_vars=["country", "iso_code", "year"],
            var_name="Fuente de Energía",
            value_name="Electricidad Generada (TWh)"
        )
        df_energy_sources = df_energy_sources[df_energy_sources["Electricidad Generada (TWh)"] > 0.000001]
    
    return df_energy_sources, df_demand


def predict_electricity_demand(df, country="World", years=10):
    # Filtrar datos del país y eliminar valores NaN
    df_filtered = df[df["country"] == country][["year", "electricity_demand"]].dropna()

    # Filtrar datos desde el año 2000 en adelante
    df_filtered = df_filtered[df_filtered["year"] >= 2000]

    # Eliminar valores negativos
    df_filtered = df_filtered[df_filtered["electricity_demand"] >= 0]

    # Ordenar por año
    df_filtered = df_filtered.sort_values(by="year")

    if df_filtered.empty:
        return pd.DataFrame(columns=["ds", "yhat", "yhat_lower", "yhat_upper"])

    # Renombrar columnas para Prophet
    df_filtered.rename(columns={"year": "ds", "electricity_demand": "y"}, inplace=True)

    # Convertir la columna de años a datetime para Prophet
    df_filtered["ds"] = pd.to_datetime(df_filtered["ds"], format="%Y")

    # Obtener el último valor real de la serie y el último año
    last_real_value = df_filtered["y"].iloc[-1]
    last_real_year = df_filtered["ds"].max()

    # Crear y entrenar el modelo Prophet con datos desde 2000
    model = Prophet()
    model.fit(df_filtered)

    # Generar predicciones desde el último año con datos hacia el futuro
    future = model.make_future_dataframe(periods=years, freq="Y")

    # 📌 Asegurar que solo tomamos predicciones desde el último año real en adelante
    future = future[future["ds"] >= last_real_year]

    forecast = model.predict(future)

    # 📌 Ajustar la predicción para que inicie exactamente donde terminó la serie real
    first_predicted_value = forecast["yhat"].iloc[0]
    adjustment = last_real_value - first_predicted_value

    forecast["yhat"] += adjustment
    forecast["yhat_lower"] += adjustment
    forecast["yhat_upper"] += adjustment

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

def predict_energy_mix(df, country="World", years=20):  # Aumentamos los años de predicción
    # Filtrar datos del país y eliminar valores NaN
    df_filtered = df[df["country"] == country][["year", "renewables_share_elec", "fossil_share_elec"]].dropna()

    # Filtrar datos desde el año 2000 en adelante
    df_filtered = df_filtered[df_filtered["year"] >= 2000]

    # Ordenar por año
    df_filtered = df_filtered.sort_values(by="year")

    if df_filtered.empty:
        return pd.DataFrame(columns=["ds", "renewables_yhat", "fossil_yhat"])

    # Convertir la columna de años a datetime para Prophet
    df_filtered["ds"] = pd.to_datetime(df_filtered["year"], format="%Y")

    # Predecir participación de renovables
    df_renewables = df_filtered[["ds", "renewables_share_elec"]].rename(columns={"renewables_share_elec": "y"})
    model_renewables = Prophet()
    model_renewables.fit(df_renewables)

    future = model_renewables.make_future_dataframe(periods=years, freq="Y")
    forecast_renewables = model_renewables.predict(future)

    # Predecir participación de fósiles
    df_fossil = df_filtered[["ds", "fossil_share_elec"]].rename(columns={"fossil_share_elec": "y"})
    model_fossil = Prophet()
    model_fossil.fit(df_fossil)

    forecast_fossil = model_fossil.predict(future)

    # Unir ambas predicciones en un solo DataFrame
    forecast = pd.DataFrame({
        "ds": forecast_renewables["ds"],
        "renewables_yhat": forecast_renewables["yhat"],
        "fossil_yhat": forecast_fossil["yhat"]
    })

    return forecast