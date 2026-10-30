# (10) Calculate bacterial population growth over time.

import numpy as np
t = np.arange(0, 121, 20)
population = 100 * 2**(t / 20)
print("Time Points:")
print(t)
print("Population:")
print(population)
print("Final Population is",
      population[-1] / population[0],
      "times larger than the starting population.")
print("Time points when population is above 1000:")
print(t[population > 1000])
