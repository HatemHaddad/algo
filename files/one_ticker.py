# Import yfinance package

import yfinance as yf

# Import matplotlib for plotting

import matplotlib.pyplot as plt

# Set the start and end date

start_date = '1990-01-01'
end_date ='2021-07-31'

# Set the ticker

ticker = 'AMZN'

# Get the data

data = yf.download(ticker,start_date,end_date)

# Print 5 rows

print(data.tail())

# Plot adjusted close price data

data['Adj Close'].plot(figsize=(10,4))

# Defile the label for the title of the figure

plt.title("Adjusted Close Price of %s" % ticker, fontsize = 16)

# Define the labels for x-axis and y-axis

plt.ylabel('Price', fontsize = 14)
plt.xlabel('Year', fontsize = 14)

# Plot the grid lines

plt.grid(which="major", color = "k", linestyle = "-.", linewidth = 0.5)

# Show the plot

plt.show()
