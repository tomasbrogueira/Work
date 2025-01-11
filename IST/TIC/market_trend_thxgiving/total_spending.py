# make an histogram of the total spending of the customers in the dataset
# The histogram is saved in the folder IST/TIC/market_trend_thxgiving/figures

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Number of shoppers.csv')

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(data['Purchase'], bins=30, color='skyblue', edgecolor='black')
plt.title('Total Spending of Customers', fontsize=16)
plt.xlabel('Purchase Amount', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.show()

