import pandas as pd

def load_data(filepath="data/owid-energy-data.csv", melt=True):
    # Cargar datos
    df = pd.read_csv(filepath)

    # Filtrar solo países (iso_code con 3 letras) y "World"
    df = df[(df["iso_code"].str.len() == 3) | (df["country"] == "World")]

    # Seleccionar solo columnas relevantes para generación de electricidad
    electricity_cols = [col for col in df.columns if col.endswith("_electricity") and not col.endswith("per_capita_electricity")]
    
    # Crear DataFrame solo con fuentes de electricidad (para el primer gráfico)
    df_energy_sources = df[["country", "iso_code", "year"] + electricity_cols].copy()

    # Crear DataFrame con generación y demanda eléctrica (para el segundo gráfico)
    df_demand = df[["country", "iso_code", "year", "electricity_generation", "electricity_demand"]].copy()

    # **Filtrar desde 1985 para df_energy_sources**
    df_energy_sources = df_energy_sources[df_energy_sources["year"] >= 1985]

    # **Filtrar desde 2000 para df_demand**
    df_demand = df_demand[df_demand["year"] >= 2000]

    # Si melt=True, transformar solo df_energy_sources (no df_demand)
    if melt:
        df_energy_sources = df_energy_sources.melt(
            id_vars=["country", "iso_code", "year"],
            var_name="Fuente de Energía",
            value_name="Electricidad Generada (TWh)"
        )
        df_energy_sources = df_energy_sources[df_energy_sources["Electricidad Generada (TWh)"] > 0.000001]  # Filtrar valores muy bajos

    return df_energy_sources, df_demand
