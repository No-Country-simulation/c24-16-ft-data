import pandas as pd

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
