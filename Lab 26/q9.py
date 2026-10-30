# (9) Calculate log2 and percentage of counts for 5 genes without using loops.

import numpy as np
counts = np.array([100, 200, 300, 400, 500])
print("Gene Counts:")
print(counts)
log_values = np.round(np.log2(counts), 2)
print("Log2 Values:")
print(log_values)
percentage = np.round((counts / np.sum(counts)) * 100, 1)
print("Percentage of Total Count:")
print(percentage)
