# (8) Calculate average, highest, lowest, numbers above 20, and scores below 20.

import numpy as np
arr = np.array([10, 25, 30, 15, 45, 20, 35, 12, 50, 18])
print("Array:", arr)
print("Average:", np.mean(arr))
print("Highest Score:", np.max(arr))
print("Lowest Score:", np.min(arr))
print("Count Above 20:", np.sum(arr > 20))
print("Scores Below 20:", arr[arr < 20])
