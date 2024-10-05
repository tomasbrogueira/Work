import pandas as pd

# Your dataset
data = {
    'Y1': [0.2, 0.1, 0.2, 0.9, -0.3, -0.1, -0.9, 0.2, 0.7, -0.3],
    'Y2': [0.5, -0.4, -0.1, 0.8, 0.3, -0.2, -0.1, 0.5, -0.7, 0.4],
    'Y3': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
}

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Covariance matrix (for Y1 and Y2)
cov_matrix = df[['Y1', 'Y2']].cov()

# Correlation matrix (for Y1 and Y2)
corr_matrix = df[['Y1', 'Y2']].corr()

# Seing non diagonal elements of covariance matrix
print(corr_matrix.iloc[0,1])

print("Covariance Matrix:\n", cov_matrix)
print("\nCorrelation Matrix:\n", corr_matrix)
