import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'y1': [0.22, 0.06, 0.16, 0.21, 0.01, 0.30, 0.76, 0.86, 0.93, 0.47, 0.73, 0.89],
    'y_out': ['C', 'B', 'C', 'B', 'C', 'B', 'A', 'A', 'C', 'C', 'A', 'B']
}

# Convert to DataFrame
df = pd.DataFrame(data)

classes = ['A', 'B', 'C']

# Set up bins for the histogram
bins = np.arange(0, 1.2, 0.2)  # [0, 0.2[, [0.2, 0.4[, ..., [0.8, 1.0[

# Calculate the total number of entries for each class
total_entries_per_class = df['y_out'].value_counts()
total_entries = df.shape[0]

# Draw a class conditional histogram of y1 and stack each above the other in the same plot with different colors so that height is the sum height of all classes
plt.figure(figsize=(10, 6))

# Initialize cumulative heights to zero
cumulative_heights = np.zeros(len(bins) - 1)

# Define the width of the bars with some spacing
bar_width = 0.15

for i, class_value in enumerate(classes):
    subset = df[df['y_out'] == class_value]['y1']
    heights, _ = np.histogram(subset, bins=bins)
    relative_heights = heights / total_entries
    plt.bar(bins[:-1] + bar_width / 2, relative_heights, width=bar_width, bottom=cumulative_heights, alpha=0.6, label=f"Class {class_value}", align='center')
    cumulative_heights += relative_heights

plt.title("Class Conditional Histogram of y1")
plt.xlabel("y1")
plt.ylabel("Relative Frequency")
plt.legend()

# Add horizontal grid lines
plt.grid(axis='y', alpha=0.5)

plt.show()