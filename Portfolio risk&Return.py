import yfinance as yf 
import numpy as np 

# Define tickers of assets in the portfolio 
tickers = ['AAPL', 'MSFT', 'GOOG'] 
# Example tickers for 3 assets 
# Fetch historical data from Yahoo Finance
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")['Adj Close'] 
# Calculate daily returns
returns = data.pct_change().dropna() 
# Define weights of assets in the portfolio 
weights = np.array([0.4, 0.3, 0.3]) 
# Example weights for 3 assets 
# Calculate mean returns of assets 
expected_returns = returns.mean() 
# Calculate covariance matrix of returns 
covariance_matrix = returns.cov()
# Calculate portfolio expected return 
portfolio_return = np.dot(weights, expected_returns) 
# Calculate portfolio risk (standard deviation) 
portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights))) 
print("Portfolio Expected Return:", portfolio_return) 
print("Portfolio Risk (Standard Deviation):", portfolio_risk)