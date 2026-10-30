# (7) Suppress scientific notation using set_printoptions().

import numpy as np
np.set_printoptions(suppress=True)
arr = np.array([1e10, 2e10, 3e10, 4e10])
print("Array without Scientific Notation:")
print(arr)
