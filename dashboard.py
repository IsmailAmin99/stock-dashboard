#import libraries 
import dash     #for building the UI
from dash import dcc, html, Input, Output   #components for interactivity
import plotly.express as px     #plotly : data visualization
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

    #stock obj
    stock = yf.Ticker(ticker)
    df = stock.history(period = period)     #fetching historical data