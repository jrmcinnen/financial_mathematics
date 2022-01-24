"""
Estimation

Estimating the values needed in binomial pricing 
based on previous stock prices 
"""
import pandas as pd
import numpy as np

TRAIDING_DAYS = 252

# Read the stock price data
def read_file(file_name='Data/IBM.csv'):
    try:
        data = pd.read_csv(file_name, sep=',', header='infer', quotechar='\"')
        return [data, True]
    except:
        return [[], False]

def main():
    data, flag = read_file()
    if not flag:
        print("Data could not be read.")
    else:
        print("Data read succesfully.\n")
        
        # Pick needed values to a numpy array
        S = pd.DataFrame(data[["Adj Close"]]).to_numpy()
        N = np.shape(S)[0]
        
        # Store the values to be summed
        s_i = np.zeros(N-1)
        for i in range(N-1):
            s_i[i] = np.log(S[i+1]/S[i])
        
        # Compute expected daily returns and variance
        v_d = 1/N*sum(s_i)     
        sigma_d = 1/(N-1)*sum((s_i-v_d*np.ones(len(s_i)))**2)
        
        print(f'v_d = {v_d}')
        print(f'sigma_d = {sigma_d}\n')
        
        # Compute the annual values
        v = v_d*TRAIDING_DAYS
        sigma = sigma_d*TRAIDING_DAYS
        
        print("Annual return and variance are:")
        print(f'v = {v}')
        print(f'sigma = {sigma}\n')
        
        # Estimate the parameters
        dt = 1/TRAIDING_DAYS
        q = 1/2+1/2*1/(np.sqrt(sigma/(v**2*dt)+1))
        U = np.exp(np.sqrt(sigma*dt+(v*dt)**2))
        D = 1/U
        
        print("Estimated parameters are:")
        print(f'q = {q}')
        print(f'U = {U}')
        print(f'D = {D}\n')
        
        # Estimate the parameters using approximate formulas
        q_app = 1/2+1/2*v*np.sqrt(dt/sigma)
        U_app = np.exp(np.sqrt(sigma*dt))
        D_app = np.exp(-np.sqrt(sigma*dt))
        
        print("Estimated parameters using approximated formulas are:")
        print(f'q_approx = {q_app}')
        print(f'U_approx = {U_app}')
        print(f'D_approx = {D_app}\n')

main()
