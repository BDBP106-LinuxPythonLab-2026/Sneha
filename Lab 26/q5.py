# (5) Create a new array containing the maximum of respective elements in two arrays.

import numpy as np
def maximum_array(a, b):
    return np.maximum(a, b)
a = np.array([1, 2])
b = np.array([0, 5])
c = maximum_array(a, b)
print("Array a:", a)
print("Array b:", b)
print("Maximum Array:", c)
