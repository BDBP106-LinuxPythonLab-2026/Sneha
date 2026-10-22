"""Write a function population_growth(initial,rate, time) that defines an inner function
exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
represents the initial population and N(t) is population after time t. The inner function
returns the population after time, and the outer function rounds and prints it (already
done in Lab 21, copy code to Lab22 folder)."""

import math
def population_growth(initial,rate,time):
    def exponential_growth():
        return initial*math.exp(time*rate)
    population = exponential_growth()
    print("Population after time:",round(population))
# Test case
population_growth(1000, 0.05, 10)
