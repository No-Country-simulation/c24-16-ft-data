from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scripts.data_processing import load_data
from scripts.data_processing import predict_electricity_demand
from scripts.data_processing import predict_energy_mix


df_melted, df_wide = load_data()

def register_callbacks(app):
    @app.callback(
        Output('energy-race-chart', 'figure'),
        [Input('year-slider', 'value'), Input('country-dropdown', 'value')]
    )
    def update_energy_sources_chart(selected_year, selected_country):
        if selected_country == "Mundo":
            selected_country = "World"
        df_filtered = df_melted[(df_melted["year"] == selected_year) & (df_melted["country"] == selected_country)]
        df_top10 = df_filtered.nlargest(10, "Electricidad Generada (TWh)")
        
        if df_top10.empty:
            return px.bar(title=f"No hay datos disponibles para {selected_country} en {selected_year}")
        
        fig = px.bar(df_top10, x="Electricidad Generada (TWh)", y="Fuente de Energía", 
                    orientation='h', text="Electricidad Generada (TWh)", 
                    title=f"Top 10 Fuentes de Energía en {selected_country} en {selected_year}",
                    labels={"Fuente de Energía": "Fuente", "Electricidad Generada (TWh)": "Generación (TWh)"})
        
        fig.update_layout(yaxis={'categoryorder': 'total ascending'})
        return fig
    
    @app.callback(
        Output('generation-vs-demand-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_demand_chart(selected_country):
        if selected_country == "Mundo":
            selected_country = "World"
        df_filtered = df_wide[(df_wide["country"] == selected_country) & (df_wide["year"] >= 2000)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_filtered["year"], y=df_filtered["electricity_demand"], mode="lines+markers", name="Demanda de Electricidad"))
        fig.add_trace(go.Scatter(x=df_filtered["year"], y=df_filtered["electricity_generation"], mode="lines+markers", name="Generación de Electricidad"))
        
        fig.update_layout(title="Generación vs. Demanda de Electricidad", xaxis_title="Año", yaxis_title="TWh")
        return fig

    @app.callback(
        Output('efficiency-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_efficiency_chart(selected_country):
        df_filtered = df_wide[df_wide["country"] == selected_country]
        fig = go.Figure(go.Scatter(x=df_filtered["year"], y=df_filtered["efficiency"], mode="lines+markers", name="Eficiencia"))
        fig.update_layout(title="Eficiencia de Generación Eléctrica", xaxis_title="Año", yaxis_title="Eficiencia")
        return fig
    
    @app.callback(
        Output('growth-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_growth_chart(selected_country):
        df_filtered = df_wide[df_wide["country"] == selected_country]
        fig = go.Figure(go.Bar(x=df_filtered["year"], y=df_filtered["generation_growth"], name="Crecimiento (%)"))
        fig.update_layout(title="Crecimiento Anual de Generación Eléctrica", xaxis_title="Año", yaxis_title="Crecimiento (%)")
        return fig
    
    @app.callback(
        Output('carbon-intensity-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_carbon_intensity_chart(selected_country):
        df_filtered = df_wide[df_wide["country"] == selected_country]
        fig = go.Figure(go.Scatter(x=df_filtered["year"], y=df_filtered["carbon_intensity_elec"], mode="lines", name="Intensidad de CO₂"))
        fig.update_layout(title="Intensidad de CO₂ en Generación Eléctrica", xaxis_title="Año", yaxis_title="CO₂ por TWh")
        return fig
    
    @app.callback(
        Output('per-capita-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_per_capita_chart(selected_country):
        df_filtered = df_wide[df_wide["country"] == selected_country]
        fig = go.Figure(go.Scatter(x=df_filtered["year"], y=df_filtered["electricity_demand_per_capita"], mode="lines", name="Consumo per cápita"))
        fig.update_layout(title="Consumo Eléctrico per cápita", xaxis_title="Año", yaxis_title="kWh por persona")
        return fig
    
    @app.callback(
        Output('renewables-fossil-pie-chart', 'figure'),
        [Input('country-dropdown', 'value'), Input('year-slider-renewables', 'value')]  
    )
    def update_pie_chart(selected_country, selected_year):
        df_filtered = df_wide[(df_wide["country"] == selected_country) & (df_wide["year"] == selected_year)]
        
        if df_filtered.empty:
            return go.Figure()

        labels = ["Renovable", "Fósil"]
        values = [df_filtered["renewables_share_elec"].values[0], df_filtered["fossil_share_elec"].values[0]]
        
        fig = px.pie(
            names=labels, 
            values=values, 
            title=f"Proporción de Energía Renovable vs. Fósil en {selected_country} ({selected_year})"
        )
        return fig


    
    @app.callback(
        Output('world-map-chart', 'figure'),
        [Input('year-slider-map', 'value')]
    )
    def update_world_map(selected_year):
        df_filtered = df_wide[(df_wide["year"] == selected_year) & (df_wide["iso_code"].notna())]
        
        # Obtener valores mínimo y máximo para la escala de colores considerando solo países con código ISO
        min_val = df_filtered["electricity_generation"].min()
        max_val = df_filtered["electricity_generation"].max()
        
        fig = px.choropleth(
            df_filtered,
            locations="iso_code",
            color="electricity_generation",
            hover_name="country",
            color_continuous_scale="Viridis",
            title=f"Generación Eléctrica por País en {selected_year}",
            labels={"electricity_generation": "Generación (TWh)"},
            range_color=[min_val, max_val]  # Ajustar la escala de colores dinámicamente
        )
        fig.update_geos(projection_type="natural earth")
        fig.update_layout(height=1000)  # Ajustar el tamaño del mapa
        return fig
    
    @app.callback(
        Output('forecast-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_forecast_chart(selected_country):
        # Obtener el último año con datos reales
        last_real_year = df_wide[df_wide["country"] == selected_country]["year"].max()

        # Obtener predicción de Prophet
        forecast = predict_electricity_demand(df_wide, country=selected_country)

        # 📌 Filtrar la predicción SOLO para años futuros al último año con datos reales
        forecast_filtered = forecast[forecast["ds"].dt.year > last_real_year]

        # Crear figura
        fig = go.Figure()

        # 📌 Agregar predicción (solo años futuros)
        fig.add_trace(go.Scatter(
            x=forecast_filtered["ds"],
            y=forecast_filtered["yhat"],
            mode="lines",
            name="Predicción",
            line=dict(color="blue", dash="dash")
        ))

        # 📌 Agregar límites de confianza
        fig.add_trace(go.Scatter(
            x=forecast_filtered["ds"],
            y=forecast_filtered["yhat_lower"],
            mode="lines",
            line=dict(color="red", dash='dot'),
            name="Límite Inferior"
        ))

        fig.add_trace(go.Scatter(
            x=forecast_filtered["ds"],
            y=forecast_filtered["yhat_upper"],
            fill="tonexty",
            mode="lines",
            line=dict(color="green", dash='dot'),
            name="Límite Superior"
        ))

        # 📌 Mostrar el país en el título
        fig.update_layout(
            title=f"Predicción de Demanda de Electricidad en {selected_country}",
            xaxis_title="Año",
            yaxis_title="TWh",
            legend_title="Leyenda"
        )

        return fig
    
    @app.callback(
        Output('energy-mix-pie-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_energy_mix_pie(selected_country):
        # Obtener predicción de mezcla energética
        forecast = predict_energy_mix(df_wide, country=selected_country)

        # Filtrar SOLO el año 2030
        forecast_selected = forecast[forecast["ds"].dt.year == 2030]

        # Si no hay datos para el 2030, devolver gráfico vacío
        if forecast_selected.empty:
            return go.Figure()

        # Obtener valores de predicción
        renewables = forecast_selected["renewables_yhat"].values[0]
        fossils = forecast_selected["fossil_yhat"].values[0]

        # Crear Pie Chart
        fig = go.Figure(data=[go.Pie(
            labels=["Renovables", "Fósiles"],
            values=[renewables, fossils],
            hole=0.4  # Hacerlo tipo "donut"
        )])

        # Configurar título
        fig.update_layout(
            title=f"Predicción de Mezcla Energética en {selected_country} (2030)",
        )

        return fig