#import libraries 
import dash   #for building the UI
from dash import dcc, html, Input, Output   #components for interactivity
import plotly.express as px    #plotly: data visualization
import yfinance as yf

#initialize the app
app = dash.Dash(__name__)

#terminal display 
print("✅ Dash app is starting...")

#define layout 
app.layout = html.Div
([
    #title -> html.H1 = header 
    html.H1("Isma'il's Stock Data Visualization", style = {"textAlign" : "center", "color" : "#4CAF50",
        "fontSize": "36px", "marginBottom": "20px"} ),

    #Intro to the project: -> html.P = paragraph
    html.P("The goal of this webpage is to visualize stock data with various graphs for analysis", 
           style = {"textAlign" : "left"}, id = "Description"),
    
    #User Input section:
    html.Div
    ([
        dcc.Input
        (
        id = "stock-input", 
        type = "text",
        value = "AAPL", #default ticker
        debounce = True, 
        placeholder = "Enter a stock symbol/ticker...",
        style = {"padding": "10px", "fontSize" : "16px", "borderRaduis" : "5px"
                 "border": "1px solid #ccc", "marginRight": "10px"}
        ),

        html.Button("Submit", id = "submit-button", style = {
            "fontsize" : "10px", "borderRadius": "5px", 
            "backgroundColor": "#4CAF50", "color": "white", "cursor": "pointer"})
    ])
])

print("✅ Layout has been assigned and initialized")

if __name__ == '__main__':
    print("✅ Running the Dash app server...")
    app.run_server(debug = True)