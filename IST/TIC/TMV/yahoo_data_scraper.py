import yfinance as yf

# Define the stock ticker and time range
ticker = "TMV"  # Replace "TMV" with the specific stock ticker you need
start_date = "2010-01-01"
end_date = "2023-12-31"

# Fetch historical data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Display the data
print(stock_data)

stock_data.to_csv("TMV_data_yearly.csv")
