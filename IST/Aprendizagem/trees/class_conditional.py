import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# Your dataset
data = {
    'Y1': [0.2, 0.1, 0.2, 0.9, -0.3, -0.1, -0.9, 0.2, 0.7, -0.3],
    'Y2': [0.5, -0.4, -0.1, 0.8, 0.3, -0.2, -0.1, 0.5, -0.7, 0.4],
    'Y3': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
}

# Convert to pandas DataFrame
df = pd.DataFrame(data)

classes = df['Y3'].unique()
colors = ['blue', 'green', 'red']  # Different colors for each class

# 1. Plot: Histogram for each class
plt.figure(figsize=(10, 6))
for i, class_value in enumerate(classes):
    subset = df[df['Y3'] == class_value]['Y2']
    plt.hist(subset, bins=5, alpha=0.6, color=colors[i], label=f"Class {class_value}", density=True)
plt.title("Histogram of Y2 for Each Class in Y3")
plt.xlabel("Y2")
plt.ylabel("Density")
plt.legend()
plt.show()

# 2. Plot: KDE for each class
plt.figure(figsize=(10, 6))
for i, class_value in enumerate(classes):
    subset = df[df['Y3'] == class_value]['Y2']
    sns.kdeplot(subset, label=f"Class {class_value}", color=colors[i])
plt.title("KDE of Y2 for Each Class in Y3")
plt.xlabel("Y2")
plt.ylabel("Density")
plt.legend()
plt.show()

# 3. Plot: Fitted Gaussian curves for each class
plt.figure(figsize=(10, 6))
for i, class_value in enumerate(classes):
    subset = df[df['Y3'] == class_value]['Y2']
    mean, std_dev = norm.fit(subset)  # Fit Gaussian distribution
    xmin, xmax = plt.xlim((-2,2))
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)  # Probability density function
    plt.plot(x, p, color=colors[i], linestyle='dashed', label=f"Class {class_value}")
plt.title("Fitted Gaussian Distribution of Y2 for Each Class in Y3")
plt.xlabel("Y2")
plt.ylabel("Density")
plt.legend()
plt.show()
