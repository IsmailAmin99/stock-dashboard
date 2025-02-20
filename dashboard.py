import dash
from dash import dcc, html

# Initialize Dash app
app = dash.Dash(__name__)

# Print confirmation that Dash is starting
print("✅ Dash app is starting...")

#define layout of webpage
app.layout = html.Div([
    
    #title:
    html.H1("Isma'il's Stock Dashboard", style={"textAlign": "center", "color": "#4CAF50",
             "fontSize" : "36px", "marginBottom" : "20px" }),
    
    #webpage/project descr:
    html.P("The goal of this project is to trying making an interactive stock dashboard", id="test-text"),


    
])

print("✅ Layout has been assigned.")

# Run the Dash app
if __name__ == '__main__':
    print("✅ Running the Dash server...")
    app.run_server(debug=True)
