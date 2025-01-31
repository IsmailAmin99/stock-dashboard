# Import libraries:
from flask import Flask, jsonify
import yfinance as yf

# Initialize the Flask app
app = Flask(__name__)

#Define a route to fetch stock data dynamically based on ticker
@app.route('/sotck/,ticker>')
def get_stock_data(ticker):
    """
    This funct retrieves historical data for the given ticker
    - fetches last month of stock history using Yahoo Finance
    - returns data in JSON format 
    """

    stock = yf.Ticker(ticker) #stock object 
    data = stock.history(period = "1mo")
    
    # Convert the DataFrame to a dict so Flask can return it as JSON
    return jsonify(data.to_dict())

# Run Flask app 
if __name__ == '__main__':
    app.run(debug = True) #run app in debug mode for developments
    