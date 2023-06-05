import yfinance as yf
import pandas as pd
from datetime import date, timedelta
import boto3
import io

# Define the asset symbols and their aliases
assets = {
    'SPY': 'SP500',
    'EFA': 'WORLDEQUITIES',
    'EEM': 'EMERGINGMARKETS',
    'VNQ': 'REALESTATE',
    'IEF': '10YTREASURY',
    'TIP': 'LINKERS',
    'LQD': 'IGBONDS',
    'HYG': 'HYBONDS'
}

# Define the allocations for each asset in the portfolio
allocations = {
    'SPY': 0.6,
    'EFA': 0.3,
    'EEM': 0.1,
    'VNQ': 0.4,
    'IEF': 0.3,
    'TIP': 0.3,
    'LQD': 0.1,
    'HYG': 0.1
}

# Define the start and end dates for the historical data
end_date = date.today()
start_date = end_date - timedelta(days=5*365)

# Create an empty DataFrame to store the historical prices
portfolio_prices = pd.DataFrame()

# Loop through each asset
for asset, alias in assets.items():
    # Download historical price data for the asset
    data = yf.download(asset, start=start_date, end=end_date)
    
    # Extract the adjusted close prices
    prices = data['Adj Close']
    
    # Calculate the daily returns
    returns = prices.pct_change().dropna()
    
    # Get the allocation for the current asset
    allocation = allocations[asset]
    
    # Multiply the returns by the asset's allocation percentage
    weighted_returns = returns * allocation
    
    # Add the weighted returns to the portfolio prices DataFrame with the asset alias as the column header
    portfolio_prices[alias] = weighted_returns

# Calculate the daily overall return of the portfolio
portfolio_prices['Portfolio'] = portfolio_prices.sum(axis=1)

# Save the portfolio data to a CSV file with aliases as column headers
csv_buffer = io.StringIO()
portfolio_prices.columns = [assets.get(col, col) for col in portfolio_prices.columns]
portfolio_prices.to_csv(csv_buffer)

# Upload the CSV file to S3
s3 = boto3.resource('s3')
bucket_name = 'big-data-cloud-project-2023'
object_key = 'read/portfolio_returns.csv'
s3.Object(bucket_name, object_key).put(Body=csv_buffer.getvalue())

print(f"CSV file uploaded to S3: s3://{bucket_name}/{object_key}")
