% Consider the following structured knock-out option. 
% The option has five observation
% dates ti = 1, 2, 3, 4, 5 years after t0. On those dates the payoff 
% is max(Si - K, 0). Moreover, if Si < 0.7 × St0, 
% the contract is terminated after paying the (possible)
% payoff for that observation date.

% Monte Carlo simulation to price this structured barrier option

clear all;



S0 = 100;    % The current stock price.
K = 110;      % Strike price.
T = 5;       % Time to maturity.
dt = 1/255;  % We observe the price on daily basis.
n = 255;     % prices in one path
r = 0.03;    % Risk-free interest rate.
sigma = 0.3;   % Volatility.
m = 1e5;     % Number of simulations.


S = zeros(m,T*n);
Sa = zeros(m,T*n);
S(:,1) = S0; Sa(:,1) = S0;

s_next =@(S0,eps) S0*exp((r-1/2*sigma^2)*dt+sigma*sqrt(dt)*eps);
payoff =@(St,T) exp(-r*T)*max(St-K,0);

terminations = zeros(2*m,T);
V_tau = zeros(m,T);
Va_tau = zeros(m,T);

for i=1:m
    epsilon = randn(1,T*n);
    for j=1:T*n
        if mod(j,n) == 0
           t = j/n;
           V_tau(i,t) = payoff(S(i,j),t);
           if S(i,j) < 0.7*S0
                terminations(i,t) = 1;
                break
           end
        end
        S(i,j+1) = s_next(S(i,j),epsilon(j));
    end
    for k=1:T*n
       if mod(k,n) == 0
           t = k/n;
           Va_tau(i,t) = payoff(Sa(i,k),t);
           if Sa(i,k) < 0.7*S0
               terminations(i+m,t) =1;
               break
           end
        end
        Sa(i,k+1) = s_next(Sa(i,k),-epsilon(k));
    end
    V(i) = sum(V_tau(i,:));
    Va(i) = sum(Va_tau(i,:));
    W(i) = 0.5*(V(i)+Va(i));
end

% standard monte carlo
standard_price = 1/m*sum(V)
% antithetic version
antithetic_price = 1/m*sum(W)
% termination percentages at each observation point
terminations_percentage = sum(terminations,1)/(2*m)
not_terminated_percentage = 1-sum(terminations_percentage)

