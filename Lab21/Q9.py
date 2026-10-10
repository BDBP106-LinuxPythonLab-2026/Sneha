"""Write a function population_growth(initial,rate, time) that defines an inner function exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
represents the initial population and N(t) is population after time t. The inner function
returns the population after time, and the outer function rounds and prints it"""

import math
initial = float(input("Enter initial population: "))
rate = float(input("Enter growth rate: "))
time = float(input("Enter time: "))
def population_growth(initial,rate,time):
    def exponential_growth():
        return initial*math.exp(rate*time)
    population = exponential_growth()
    print("Population after time: ", round(population))
population_growth(initial,rate,time)