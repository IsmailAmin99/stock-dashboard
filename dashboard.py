import dash #frontend webpage 
from dash import dcc, html, Input, Output #for styling and editing webpage output 
import plotly.express as px #plotly graph
import yfinance as yf #stock info
from cachetools import TTLCache, cached #for caching the stock data -> ensures we don't fetch data too often 

# Initialize Dash app
app = dash.Dash(__name__)

#create a cache for storing stock data for 1hr (3600secs)
stock_cache = TTLCache(maxsize = 100, ttl = 3600)

@cached(stock_cache)

#function to get stock data weekly:
def get_stocks(ticker = "AAPL"):
    stock = yf.Ticker(ticker)
    df = stock.history(period = "3mo", interval = "1wk") 

    #checking to see if there's any data 
    if df.empty:
        print("Didn't get anything.")
        return None
    return df

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

    #webpage graph section:
    html.Div([
        dcc.Graph(id = "stock-graph", figure = px.line(title = "Enter a stock ticker and click Submit.")),
    ],
        
    #graph styling:
    style = {"width": "80%", "margin": "auto"}
    ),

    #auto-refreshing the graph every week:
    dcc.Interval(
        id = "interval-update",
        interval = 7 * 24 * 60 * 60 * 1000, #7 days in milliseconds
        n_intervals = 0
    )
])


#callback for updating the graph
@app.callback(
    Output("stock-graph", "figure"),
    Input("submit-button", "n_clicks"),
    Input("stock-input", "value")
)

def update_graph(n_clicks, ticker):
    df = get_stocks(ticker)
    
    if df is None:
        return px.line(title = f"No data available for {ticker}")
    
    fig = px.line(df, x = df.index, y = "Close", title = f"Daily Stock Prices for {ticker}")
    
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
