#  (4) Swap the first and second columns in a 3×3 random matrix.

import numpy as np
arr = np.random.randint(1, 100, (3, 3))
print("Original Matrix:")
print(arr)
arr[:, [0, 1]] = arr[:, [1, 0]]
print("After Swapping First and Second Columns:")
print(arr)
