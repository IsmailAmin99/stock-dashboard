#import libraries 
import dash   #for building the UI
from dash import dcc, html, Input, Output   #components for interactivity
import plotly.express as px    #plotly: data visualization
import yfinance as yf

#initialize the app
    #makes sure dynamically created callbacks can be recognized
app = dash.dash(__name__, suppress_callback_extension = True)

#fetch the stock data
def fetch_stockData(ticker = "AAPL", period = "1 monnth"):
    """
    fetches historical stock data for the given ticker
        - Default ticker: AAPL -> Apple
        - Default period: 1 month 
    """

    #stock object 
    stock = yf.Ticker(ticker)
    df = stock.history(period = period)   #fetching historical data

    #ensure data exists before returning
    if df.empty:
        return None
    return df



#defining the layout of the dashboard 
app.layout = html.Div
([
    #title
    html.H1("Stock Price Dashboard", style = {"textAlign": "center"}),

    html.Div
    ([
        #user input for entering wanted stock ticker
        dcc.Input
        (
            id = "stock-input", #ID used in the callback funct
            type = "text",
            value = "GOOGL", #default ticker -> Google 
            debounce = True, #reduces unnecessary updates 
            style = {"margiRight": "10px"}
        ),

        #submit button -> updates the graph 
        html.Button("Submit", id = "submit-button"),
    ],
        style = {"display": "flex", "justifyContent": "center"}),
    
])

#define callback to update the graph when user enters new stock ticker
@app.callback(
    #update graph output 
    Output("stock-graph", "figure"),

    #trigger when the submit button is clicked 
    Input("submit-button", "n_clicks"),

    #get stock ticker input 
    Input("stock-input", "value")
)

def update_graph(n_clicks, ticker):
    """
    Updates the stock graph when the user submits a new stock ticker. 
        - Fetches data for entered ticker
        - Updates graph 
    """

    df = fetch_stockData(ticker)

    #error handling for if stock data isn't found
    if df is None:
        return px.line(title = f"No data availabale for {ticker}")
    
    #create a new line chart with updated stock data
    fig = px.line(df, x = df.index, y = "Close", title = f"Stock Prices for {ticker}")

    #return updated graph
    return fig

#run the app
if __name__ == '__main__':
    app.run_server(debug=True)