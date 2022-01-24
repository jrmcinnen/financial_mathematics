# -*- coding: utf-8 -*-
"""
Black-Scholes model for call option price
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the known values
S0 = 50
sigma = 0.3
mu = 0.13
T = 1
dt = 1/255
K = 50
r = 0.13
q = 0.0
t=np.arange(0,255)*dt+dt
print(t)
num_of_steps = len(t)

# Initial containers for stock values
S = np.zeros(num_of_steps, dtype=np.float64)
S[0] = S0
epsilon = np.zeros(num_of_steps)
for i in range(1,num_of_steps):
    epsilon[i-1] = np.random.normal(0,1)
    S[i] = S[i-1]*np.exp((mu-1/2*sigma**2)*dt+sigma*epsilon[i-1]*np.sqrt(dt))    
    t[i] = t[i-1]+dt

d1 = (np.log(S/K)+(r-q+0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
d2 = (np.log(S/K)+(r-q-0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))

C1 = S*np.exp(-q*(T-t))*norm.cdf(d1)-K*np.exp(-r*(T-t))*norm.cdf(d2)

plt.plot(t,S,label="Stock price")
plt.plot(t,C1,label="Call option price")
plt.legend()
plt.show()