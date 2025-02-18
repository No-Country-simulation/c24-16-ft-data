from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from scripts.data_processing import load_data

# Cargar datos procesados correctamente
df_melted, df_wide = load_data() 

def register_callbacks(app):
    @app.callback(
        Output('energy-race-chart', 'figure'),
        [Input('year-slider', 'value'), Input('country-dropdown', 'value')]
    )
    def update_energy_sources_chart(selected_year, selected_country):
        # Convertir "Mundo" a "World" para que coincida con los datos
        if selected_country == "Mundo":
            selected_country = "World"

        # Filtrar los datos según selección
        df_filtered = df_melted[(df_melted["year"] == selected_year) & (df_melted["country"] == selected_country)]

        # Seleccionar las 10 fuentes de energía más usadas
        df_top10 = df_filtered.nlargest(10, "Electricidad Generada (TWh)")

        # Verificar que haya datos antes de graficar
        if df_top10.empty:
            return px.bar(title=f"No hay datos disponibles para {selected_country} en {selected_year}")

        # Crear gráfico
        fig = px.bar(df_top10, x="Electricidad Generada (TWh)", y="Fuente de Energía", 
                    orientation='h', text="Electricidad Generada (TWh)", 
                    title=f"Top 10 Fuentes de Energía en {selected_country} en {selected_year}",
                    labels={"Fuente de Energía": "Fuente", "Electricidad Generada (TWh)": "Generación (TWh)"},
                    range_x=[0, df_top10["Electricidad Generada (TWh)"].max() * 1.1])

        # Ajustes visuales
        fig.update_traces(marker_color="royalblue", textfont_size=10, textposition="outside", cliponaxis=False)
        fig.update_layout(yaxis={'categoryorder': 'total ascending'}, transition={'duration': 500, 'easing': 'cubic-in-out'}, bargap=0.2)

        return fig

    @app.callback(
        Output('generation-vs-demand-chart', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_demand_chart(selected_country):
        # Convertir "Mundo" a "World"
        if selected_country == "Mundo":
            selected_country = "World"

        # Filtrar datos del país seleccionado en formato ancho
        df_filtered = df_wide[df_wide["country"] == selected_country]

        # Verificar que existan datos antes de graficar
        if df_filtered.empty:
            return go.Figure(layout={"title": f"No hay datos disponibles para {selected_country}"})

        # Crear figura demanda eléctrica
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df_filtered["year"],
            y=df_filtered["electricity_demand"],
            mode="lines+markers",
            name="Demanda de Electricidad",
            line=dict(color="red", width=2),
            marker=dict(size=6)
        ))

        # Ajustar la escala del eje Y para mejorar visibilidad
        min_y = df_filtered["electricity_demand"].min()
        max_y = df_filtered["electricity_demand"].max()

        fig.update_layout(
            title=f"Demanda de Electricidad en {selected_country}",
            xaxis_title="Año",
            yaxis_title="Electricidad Demandada (TWh)",
            legend_title="Tipo",
            yaxis=dict(range=[min_y * 0.9, max_y * 1.1]),  # Ajustar escala
            dragmode="pan",  # Habilitar desplazamiento en el gráfico
            hovermode="x",  # Mejor interacción al pasar el mouse
            template="plotly_white"
        )

        return fig