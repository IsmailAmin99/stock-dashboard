import dash
from dash import dcc, html

# Initialize Dash app
app = dash.Dash(__name__)

# Print confirmation that Dash is starting
print("✅ Dash app is starting...")

# Define a test layout to check if components render
app.layout = html.Div([
    html.H1("Dash is Running!", style={"textAlign": "center", "color": "green"}),
    html.P("If you see this, Dash is working!", id="test-text"),
    dcc.Graph(id="test-graph")
])

print("✅ Layout has been assigned.")

# Run the Dash app
if __name__ == '__main__':
    print("✅ Running the Dash server...")
    app.run_server(debug=True)