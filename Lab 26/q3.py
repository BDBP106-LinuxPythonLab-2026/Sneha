# (3) Reverse the rows and columns in a 2D array.

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Original Array:")
print(arr)
print("Reverse Rows:")
print(arr[::-1, :])
print("Reverse Columns:")
print(arr[:, ::-1])

