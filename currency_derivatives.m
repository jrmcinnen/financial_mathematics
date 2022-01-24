% Pricing currency derivatives

clear all;

X0 = 0.52;
K = 0.5;
sig = 0.12;
rq = 0.04;
rb = 0.08;
T = 8/12;

d1 = (log(X0/K)+(rq-rb+1/2*sig^2)*T)/(sig*sqrt(T));
d2 = (log(X0/K)+(rq-rb-1/2*sig^2)*T)/(sig*sqrt(T));

call_price = X0*exp(-rb*T)*normcdf(d1)-K*exp(-rq*T)*normcdf(d2)

f_price = X0*exp(-rb*T)-K*exp(-rq*T)

put_price = call_price - f_price

[call_blsprice,put_blsprice] = blsprice(X0,K,rq,T,sig,rb)