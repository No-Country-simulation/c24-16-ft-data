from scripts import load_data, create_layout, register_callbacks
from dash import Dash

app = Dash(__name__)
app.layout = create_layout()

# Registrar callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)




