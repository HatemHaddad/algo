# Risk profiles of put option buyer and seller
# Buying a put option gives you the right, but not the obligation to sell the
# underlying security at the given strike price,
# within a specific time period. Therefore a put option payoff at expiration
# depends on where the underlying price is relative to
# the put option strike price.

# In this notebook, we will plot a put buyer's and a put seller's payoff
# graph for a 900 strike price put


import numpy as np
import matplotlib.pyplot as plt

# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')


# Put payoff
# We define a function put_payoff that calculates the payoff from buying a put option.
# The function takes sT which is a range of possible values of the stock price at expiration,
# the strike price of the put option and the premium of the put option as input.

# It returns a numpy array containing the profit from put option for different stock prices.
# When the stock price is less than the strike price, the profit is measured as
# the difference between strike price and stock price,
# and when the stock price is greater than the strike price then the profit is zero.
# After this, a put premium is deducted from the Profit-n-Lose(pnl) to compute the payoff.

def put_payoff(sT, strike_price, premium):
    pnl = np.where(sT < strike_price, strike_price-sT, 0)
    return pnl - premium


# Stock price
spot_price = 900

# Put strike price and cost
strike_price = 900
premium = 20

# Stock price range at the expiration of the put
# We have defined range for the stock price at expiry as +/- 10% from spot price
# Syntax: numpy.arange(start price, stop price)
sT = np.arange(0.9*spot_price, 1.1*spot_price)

payoff_long_put = put_payoff(sT, strike_price, premium)
# Plot the graph
fig, ax = plt.subplots(figsize=(8, 5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT, payoff_long_put, label='Put option buyer payoff')
plt.xlabel('Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

payoff_short_put = payoff_long_put * -1.0
# Plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT, payoff_short_put, label='Put option seller payoff', color='r')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()
