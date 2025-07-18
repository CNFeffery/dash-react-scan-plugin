import dash
from dash import html

# Import the react scan plugin
from dash_react_scan_plugin import setup_react_scan_plugin

# Enable the react scan plugin for the current app
setup_react_scan_plugin()

app = dash.Dash(__name__)

app.layout = html.Div(
    [html.Button(f"button{i}", id=f"demo-button{i}") for i in range(100)],
    style={"padding": 50},
)

if __name__ == "__main__":
    app.run(debug=True)
