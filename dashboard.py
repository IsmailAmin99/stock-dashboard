import dash
from dash import dcc, html

# Initialize Dash app
app = dash.Dash(__name__)

#define layout of webpage
app.layout = html.Div([
    
    #title:
    html.H1("Isma'il's Stock Dashboard", style={"textAlign": "center", "color": "#4CAF50",
             "fontSize" : "36px", "marginBottom" : "20px" }),
    
    #webpage/project descr:
    html.P("The goal of this project is to trying making an interactive stock dashboard. Try putting in a few stocks and see how it goes.", id="test-text"),
    
    #user input:
    html.Div([

        dcc.Input(
            id = "stock-input",
            type = "text",
            value = "AAPL", #test/default ticker
            placeholder = "Enter a ticker...", #this text will show until the user clicks into the box and types
            style = {"fontSize": "11px", "borderRadius": "5px", "border" : "2px solid #ccc",
                     "marginRight" : "10px", "padding" : "8px"}
        ),

        #button for submission:
        html.Button("Submit", id = "submit-button", style = {
            "padding": "7px 15px", "fontSize": "15px", "borderRadius" : "5px", "border" : "none",
            "backgroundColor" : "#4CAF50", "color" : "white", "cursor" : "pointer"})
    ],
    
    #input styling -> centering user input box & submit button: 
    style = {"display" : "flex", "justifyContent" : "center", "alignItems" : "center", "marginBottom": "20px"}
    ),
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
