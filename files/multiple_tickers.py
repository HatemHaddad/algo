# Import packages

import yfinance as yf
import pandas as pd

# Set the start_date and end_date

start_date = '1990-01-01'
end_date = '2021-07-31'

# Define the ticker list

ticker_list = ['FB','AAPL','AMZN','NFLX','GOOG']

# Create placeholder for data

data = pd.DataFrame(columns=ticker_list)

# Fetch the data

for ticker in ticker_list:
    data[ticker] = yf.download(ticker,start_date,end_date)['Adj Close']

# Print first 5 rows of the data

print(data.head())
