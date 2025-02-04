#import libraries 
import dash   #for building the UI
from dash import dcc, html, Input, Output   #components for interactivity
import plotly.express as px    #plotly: data visualization
import yfinance as yf

#initialize the app
app = dash.Dash(__name__)

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

#define the layout of the dashboard 
app.layout = html.Div
([
    #title
    html.H1("Stock Price Dashboard", style = {"textAlign": "center"}),

    #user input field for entering a stock ticker
    dcc.Input(id = "stock-input", type = "text", value = "AAPL", style = {"marginRight": "10px"}),
    
    #submit button
    html.Button("Submit", id = "submit-button"), 

    #graph that will display stock data
    dcc.Graph(id = "stock-graph"),
])