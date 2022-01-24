% Pricing of down-and-in and down-and-out call option
% using Monte Carlo method

clear all;

S0 = 50; S(1) = S0; Sa(1) = S0;   % The current stock price.
K = 50;      % Strike price.
T = 1;       % Time to maturity.
dt = 1/252;  % We observe the price on daily basis.
n = 252;     % Number of prices in one path.
r = 0.05;    % Risk-free interest rate.
sigma = 0.3;   % Volatility.
X = 45;      % The barrier.
m = 1e5;     % Number of simulations.

s_next =@(S0,eps) S0*exp((r-1/2*sigma^2)*dt+sigma*sqrt(dt)*eps);
payoff =@(St) exp(-r*n*dt)*max(St-K,0);

% method for pricing down and out option.
for i=1:m
    for j=1:n
        epsilon(j) = randn;
        S(j+1) = s_next(S(j),epsilon(j));
        Sa(j+1) = s_next(Sa(j),-epsilon(j));
    end
    S_min(i) = min(S);
    Sa_min(i) = min(Sa);
    V(i) = 0; Va(i) = 0;
    % X is the barrier that must be hit in order to get positive payoff
    if S_min(i) > X
        V(i) = payoff(S(end));
    end
    if Sa_min(i) > X
        Va(i) = payoff(Sa(end));
    end     
    W(i) = 0.5*(V(i)+Va(i));
end

% antithetic monte carlo method for down and in call option price
c_down_out = 1/m*sum(W)

% analytical solution for vanilla call option price (Black-Schooles model)
d1 = (log(S0/K)+(r-0.5*sigma^2)*T)/(sigma*sqrt(T));
d2 = d1-sigma*sqrt(T);
c_vanilla = S0*normcdf(d1)-K*exp(-r*T)*normcdf(d2)

c_down_in = c_vanilla - c_down_out