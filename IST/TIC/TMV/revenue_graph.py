import pandas as pd
import matplotlib.pyplot as plt

# Check the contents of the CSV file
try:
    with open("TMV_data_yearly.csv", 'r') as file:
        print(file.readline())  # Print the header
        print(file.readline())  # Print the first data row
except FileNotFoundError:
    print("The file TMV_data_yearly.csv was not found.")
    exit()

# Load the data with error handling
try:
    stock_data = pd.read_csv("TMV_data_yearly.csv", skiprows=3, parse_dates=["Date"])
except FileNotFoundError:
    print("The file TMV_data_yearly.csv was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("The file TMV_data_yearly.csv is empty.")
    exit()
except pd.errors.ParserError:
    print("Error parsing TMV_data_yearly.csv.")
    exit()

# Extract the year from the date
stock_data["Year"] = stock_data["Date"].dt.year

# Group the data by year and calculate the total revenue for each year
revenue_by_year = stock_data.groupby("Year")["Close"].sum()

# Plot the revenue over the years
plt.figure(figsize=(12, 6))
plt.plot(revenue_by_year.index, revenue_by_year.values, marker="o", color="b")
plt.title("Revenue of TMV Over the Years")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.grid(True)

# Save the plot as an image file
plt.savefig("revenue_over_years.png")

# Show the plot
plt.show()