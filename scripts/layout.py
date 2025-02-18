from dash import dcc, html
from scripts.data_processing import load_data

# Cargar datos procesados
df_melted, df_wide = load_data()  # 🔴 Ahora asignamos correctamente ambos valores

# Lista de países para el dropdown
countries_list = ["Mundo" if country == "World" else country for country in sorted(df_melted["country"].unique())]

def create_layout():
    return html.Div(children=[
        html.H1("Energía Global: Análisis de Generación y Consumo"),

        # Dropdown para seleccionar país o el mundo
        html.Label("Selecciona un país o el mundo:"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{"label": country, "value": "World" if country == "Mundo" else country} for country in countries_list],
            value="World",
            clearable=False,
            style={"width": "50%"}
        ),

        # Slider para seleccionar el año
        dcc.Slider(
            id='year-slider',
            min=1985,
            max=df_melted["year"].max(),
            value=2010,  
            marks={int(year): str(year) for year in range(1985, df_melted["year"].max(), 5)},
            step=1,
            tooltip={"placement": "bottom", "always_visible": True}
        ),

        # Gráfico de Top 10 Fuentes de Energía
        dcc.Graph(id='energy-race-chart'),

        html.H3("Comparación de Generación y Consumo de Electricidad"),
        dcc.Graph(id='generation-vs-demand-chart')  # Nuevo gráfico
    ])
