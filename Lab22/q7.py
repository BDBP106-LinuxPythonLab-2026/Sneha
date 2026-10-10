import time
import math

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:",end - start,"seconds")
        return result
    return wrapper
@measure_time
def population_growth(initial,rate,time):
    population = initial
    for i in range(1000000):
        population=initial*math.exp(rate*time)
    print("Population after time:",round(population))
#Test case
population_growth(1000,0.05,10)