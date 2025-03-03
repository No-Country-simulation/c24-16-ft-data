from dash import dcc, html
from scripts.data_processing import load_data

df_melted, df_wide = load_data()
countries_list = ["Mundo" if country == "World" else country for country in sorted(df_melted["country"].unique())]

def create_layout():
    return html.Div(children=[
        html.H1("Energía Global: Análisis de Generación y Consumo"),
        
        html.Label("Selecciona un país o el mundo:"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{"label": country, "value": "World" if country == "Mundo" else country} for country in countries_list],
            value="World",
            clearable=False,
            style={"width": "50%"}
        ),
        
        # Agregando nuevamente el slider de año
        dcc.Slider(
            id='year-slider',
            min=df_melted["year"].min(),
            max=df_melted["year"].max(),
            value=df_melted["year"].max(),
            marks={int(year): str(year) for year in range(df_melted["year"].min(), df_melted["year"].max() + 1, 5)},
            step=1,
            tooltip={"placement": "bottom", "always_visible": True}
        ),
        
        dcc.Graph(id='energy-race-chart'),
        dcc.Graph(id='generation-vs-demand-chart'),
        dcc.Graph(id='efficiency-chart'),
        dcc.Graph(id='growth-chart'),
        dcc.Graph(id='carbon-intensity-chart'),
        dcc.Graph(id='per-capita-chart'),
        dcc.Graph(id='renewables-fossil-pie-chart'),


        html.H3("Mapa Mundial de Generación Eléctrica"),
        dcc.Slider(
            id='year-slider-map',
            min=df_wide["year"].min(),
            max=df_wide["year"].max(),
            value=df_wide["year"].max(),
            marks={int(year): str(year) for year in range(df_wide["year"].min(), df_wide["year"].max() + 1, 5)},
            step=1,
            tooltip={"placement": "bottom", "always_visible": True}
        ),
        dcc.Graph(id='world-map-chart', style={"height": "125vh"})  # Aumentando el tamaño del mapa
    ])