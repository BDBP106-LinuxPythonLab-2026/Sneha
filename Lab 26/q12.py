# (12) Analyzing Gene Expression Heatmaps.

import numpy as np

# Create a 5x10 random array
arr = np.random.rand(5, 10) * 100
print("Original Gene Expression Matrix:")
print(arr)

# Calculate mean of each row
row_mean = np.mean(arr, axis=1, keepdims=True)

# Subtract row mean from each gene
normalized = arr - row_mean
print("\nNormalized Gene Expression Matrix:")
print(normalized)

# Calculate total expression of each sample
column_sum = np.sum(normalized, axis=0)
print("\nTotal Expression of Each Sample:")
print(column_sum)

# Set threshold
threshold = 50

# Find samples above threshold
samples = np.where(column_sum > threshold)
print("\nSamples with Total Expression Above 50:")
print(samples)
