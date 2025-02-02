import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the data tables with labels
data_table1 = pd.DataFrame({
    'Labels': ['No. of Returns', 'Average Return', 'Median Return', 'Percent Positive', 'Std. Deviation'],
    'Week After Black Friday': ['32', '0.63%', '0.39%', '65.6%', '2.08%'],
    'All Weeks': ['1716', '0.17%', '0.27%', '56.5%', '2.34%']
})

data_table2 = pd.DataFrame({
    'Labels': ['No. of Returns', 'Average Return', 'Median Return', 'Percent Positive', 'Std. Deviation'],
    'Monday': ['32', '-0.23%', '-0.16%', '40.6%', '1.94%'],
    'Tuesday': ['32', '0.10%', '-0.01%', '50.0%', '1.09%'],
    'Wednesday': ['32', '0.41%', '0.03%', '53.1%', '1.27%'],
    'Thursday': ['32', '-0.21%', '-0.11%', '40.6%', '0.97%'],
    'Friday': ['32', '0.58%', '0.42%', '78.1%', '0.95%']
})

data_table3 = pd.DataFrame({
    'Labels': ['No. of Returns', 'Average Return', 'Median Return', 'Percent Positive', 'Std. Deviation'],
    'Monday': ['1563', '0.03%', '0.07%', '53.8%', '1.27%'],
    'Tuesday': ['1700', '0.07%', '0.02%', '51.6%', '1.17%'],
    'Wednesday': ['1698', '0.04%', '0.07%', '54.5%', '1.09%'],
    'Thursday': ['1671', '0.02%', '0.05%', '53.0%', '1.16%'],
    'Friday': ['1658', '0.01%', '0.07%', '54.5%', '1.07%']
})

data_table4 = pd.DataFrame({
    'Labels': ['No. of Returns', 'Average Return', 'Median Return', 'Percent Positive', 'Std. Deviation'],
    'Black Friday Week Down 1%+': ['6', '-4.58%', '-4.74%', '33.3%', '11.00%'],
    'Black Friday Week Flat': ['14', '2.23%', '1.76%', '71.4%', '4.63%'],
    'Black Friday Week Up 1%+': ['11', '3.88%', '5.21%', '81.8%', '6.53%']
})

data_table5 = pd.DataFrame({
    'Labels': ['No. of Returns', 'Average Return', 'Median Return', 'Percent Positive', 'Std. Deviation'],
    'Black Friday Week Down 1%+': ['6', '1.60%', '1.75%', '83.3%', '3.24%'],
    'Black Friday Week Flat': ['14', '1.06%', '1.08%', '78.6%', '1.78%'],
    'Black Friday Week Up 1%+': ['11', '0.99%', '1.19%', '72.7%', '4.49%']
})

table_styles = {
    "header_bg": "#4F81BD",
    "header_text_color": "white",
    "header_fontsize": 20,
    "cell_fontsize": 20,
    "cell_bg": "#DCE6F1",
}

# Function to plot a table with alternating row colors
def plot_table_with_alternating_rows(df, title, size=(8, 3), header_height=0.2):
    fig, ax = plt.subplots(figsize=size)
    ax.axis('off')
    ax.set_title(title, fontsize=14, color=table_styles["header_bg"], weight='bold')
    
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colColours=[table_styles["header_bg"]] * len(df.columns))
    
    for key, cell in table.get_celld().items():
        cell.set_edgecolor("black")
        cell.set_linewidth(0.5)
        if key[0] == 0:
            cell.set_text_props(color=table_styles["header_text_color"], weight='bold', fontsize=table_styles["header_fontsize"])
            cell.set_height(header_height)
        else:
            cell.set_facecolor(table_styles["cell_bg"] if key[0] % 2 == 0 else "white")
            cell.set_fontsize(table_styles["cell_fontsize"])
    return fig

# Plot and save each table as an image
fig1 = plot_table_with_alternating_rows(data_table1, "S&P 500 Weekly Returns Since 1990", size=(6, 2.5), header_height=0.3)
fig2 = plot_table_with_alternating_rows(data_table2, "S&P 500 Week After Black Friday", size=(8, 3), header_height=0.2)
fig3 = plot_table_with_alternating_rows(data_table3, "S&P 500 Anytime Since 1990", size=(8, 3), header_height=0.2)
fig4 = plot_table_with_alternating_rows(data_table4, "S&P 500 Next Three Months", size=(8, 3), header_height=0.3)
fig5 = plot_table_with_alternating_rows(data_table5, "S&P 500 Rest of Year Returns", size=(8, 3), header_height=0.3)

# Output paths for each table
output_paths = [
    'C:/Users/Tomas/OneDrive/work/IST/TIC/market_trend_thxgiving/table1.png', 
    'C:/Users/Tomas/OneDrive/work/IST/TIC/market_trend_thxgiving/table2.png',
    'C:/Users/Tomas/OneDrive/work/IST/TIC/market_trend_thxgiving/table3.png',
    'C:/Users/Tomas/OneDrive/work/IST/TIC/market_trend_thxgiving/table4.png',
    'C:/Users/Tomas/OneDrive/work/IST/TIC/market_trend_thxgiving/table5.png'
]

# Save each figure
for fig, path in zip([fig1, fig2, fig3, fig4, fig5], output_paths):
    try:
        fig.savefig(path, bbox_inches="tight", dpi=300)
        print(f"Figure saved successfully at {path}")
    except Exception as e:
        print(f"Error saving figure at {path}: {e}")

plt.close('all')

output_paths
