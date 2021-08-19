# Import packages

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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

# Plot all close prices

data.plot(figsize=(10,7))

# Show the legend

plt.legend()

# Define the labelfor the title of the figure

plt.title('Adjusted Close Price', fontsize=16)

# Define the label for x-axis and y-axis

plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines

plt.grid(which='major', color='k', linestyle='-.',linewidth=0.5)
plt.show()
