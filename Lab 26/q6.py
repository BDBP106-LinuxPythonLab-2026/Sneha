# (6) Print a 3×3 random matrix up to 3 decimal places using set_printoptions().

import numpy as np
np.set_printoptions(precision=3)
arr = np.random.rand(3, 3)
print("Random 3x3 Matrix:")
print(arr)
