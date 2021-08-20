# Risk profiles of call option buyer and seller
# ===============================================
# Buying a call option gives you the right, but not the obligation,
# to buy the underlying security at the given strike price. Therefore a call
# option payoff at expiration depends on where the underlying price is relative
# to the call option strike price.

# In this code, we will plot a call buyer's and a call seller's payoff graph
# for a 900 strike price call.

import numpy as np
import matplotlib.pyplot as plt

# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')

# Call payoff
# ===========
# We define a function call_payoff that calculates the payoff from buying a call option.
# The function takes sT, a range of possible values of the stock price at expiration,
# the strike price of the call option and premium of the call option as input.

# It returns a numpy array containing the profit from call option for different the stock price.
# When the stock price is greater than the strike price, the profit is the difference between
# stock price and strike price and when the stock price is less than the strike price the profit is zero.
# After this, a call premium is deducted from the Profit-n-Loss(pnl).


def call_payoff(sT, strike_price, premium):
    pnl = np.where(sT > strike_price, sT - strike_price, 0)
    return pnl - premium


# Stock price
spot_price = 900

# Call strike price and cost
strike_price = 900
premium = 20

# Stock price range at the expiration of the call
# We have defined range for the stock price at expiry as +/- 10% from spot price
# Syntax: numpy.arange(start price, stop price)
sT = np.arange(0.9*spot_price, 1.1*spot_price)


payoff_long_call = call_payoff(sT, strike_price, premium)
# Plot the graph
fig, ax = plt.subplots(figsize=(8, 5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT, payoff_long_call, label='Call option buyer payoff')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()


payoff_short_call = payoff_long_call * -1.0
# Plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT, payoff_short_call, label='Short 940 Strike Call', color='r')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()
