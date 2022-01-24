"""
Binomial pricing,

European put option and
American put option
"""

import numpy as np


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

# Option value matrix for European put option
eu_option_value = np.zeros((m+1,m+1))
for i in range(m+1):
    eu_option_value[i,m] = np.amax(np.array([K-stock_value[i,m],0]))
                                
for i in range(m-1,-1,-1):
    for j in range(i,-1,-1):
        eu_option_value[j,i] = (p*eu_option_value[j,i+1]+(1-p)*eu_option_value[j+1,i+1])*np.exp(-r*Dt)
        
print("European option's values:")
print(eu_option_value)
print()

print(f'\nPrice for the European put option is {eu_option_value[0,0]}\n')

am_option_value = np.zeros((m+1,m+1))
for i in range(m+1):
    am_option_value[i,m] = np.amax(np.array([K-stock_value[i,m],0]))
                                
for i in range(m-1,-1,-1):
    for j in range(i,-1,-1):
        p_star = (p*am_option_value[j,i+1]+(1-p)*am_option_value[j+1,i+1])*np.exp(-r*Dt)
        am_option_value[j,i] = np.amax(np.array([p_star, K-stock_value[j,i]]))
        
print("American option's values:")
print(am_option_value)
print()

print(f'\nPrice for the American put option is {am_option_value[0,0]}')
