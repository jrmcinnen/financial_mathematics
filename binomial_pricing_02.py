"""
Binomial pricing,

European put option and
European call option using binomial distribution
"""

import numpy as np
from math import factorial


# Current stock price
S0 = 100
# Strike price
K = 105
# risk-free interest rate
r = 0.03
# Monthly changes up (U) or down (D)
U = 1.07 
D = 1/U
# Maturity time
m = 6
# Time step
Dt = 1/12
# risk-neutral probability
p = (np.exp(r*Dt)-D)/(U-D)

# Prepare the stock value matrix
stock_value = np.zeros((m+1,m+1))
stock_value[0,0] = S0
for i in range(1,m+1,):
    for j in range(1,m+1):
        stock_value[i,j] = stock_value[i-1,j-1]*D

for i in range(0,m+1):
    for j in range(i+1,m+1):
        stock_value[i,j] = stock_value[i,j-1]*U

print('Stock values:')
print(stock_value)
print()

k_prob_put = np.zeros(m+1)

for k in range(m+1):
    k_prob_put[k] = factorial(m)/(factorial(k)*factorial(m-k))*p**k*(1-p)**(m-k)*np.amax(np.array([K-S0*U**k*D**(m-k),0]))
    
put_option_price = np.sum(k_prob_put)*np.exp(-r*m*Dt)
print(f'Price for the European put option is {put_option_price}\n')

k_prob_call = np.zeros(m+1)

for k in range(m+1):
    k_prob_call[k] = factorial(m)/(factorial(k)*factorial(m-k))*p**k*(1-p)**(m-k)*np.amax(np.array([S0*U**k*D**(m-k)-K,0]))
    
call_option_price = np.sum(k_prob_call)*np.exp(-r*m*Dt)
print(f'Price for the corresponding European call option is {call_option_price}\n')
