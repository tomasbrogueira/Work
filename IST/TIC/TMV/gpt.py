import pandas as pd
import matplotlib.pyplot as plt

# Load the data, skipping the first two rows, and set the Date column
stock_data = pd.read_csv("TMV_data_yearly.csv", skiprows=3)

# Convert the 'Date' column to datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce')

# Extract the year from the 'Date' column
stock_data["Year"] = stock_data["Date"].dt.year

# Group the data by year and calculate the total revenue for each year
# Assuming "Close" column represents revenue in this case
revenue_by_year = stock_data.groupby("Year")["Close"].sum()

# Plot the revenue over the years
plt.figure(figsize=(12, 6))
plt.plot(revenue_by_year.index, revenue_by_year.values, marker="o", color="b")
plt.title("Revenue of TMV Over the Years")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
