import numpy as np
import matplotlib.pyplot as plt

# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')


#Put payoff
#We define a function put_payoff that calculates the payoff from buying a put option.
#The function takes sT which is a range of possible values of the stock price at expiration,
# the strike price of the put option and the premium of the put option as input.

# It returns a numpy array containing the profit from put option for different stock prices.
# When the stock price is less than the strike price, the profit is measured as the difference between strike price and stock price,
# and when the stock price is greater than the strike price then the profit is zero.
# After this, a put premium is deducted from the Profit-n-Lose(pnl) to compute the payoff.
