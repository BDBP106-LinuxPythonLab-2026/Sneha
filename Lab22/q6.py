import math
def population_growth(initial,rate,time):
    def exponential_growth():
        return initial*math.exp(time*rate)
    population = exponential_growth()
    print("Population after time:",round(population))
# Test case
population_growth(1000, 0.05, 10)