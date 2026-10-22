"""Write a decorator measure_time to calculate how long a function takes to run. Use it
on a function that calculates the factorial of a number. Use a test case of calculating the
factorial of 50."""

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
def factorial(n):
    return math.factorial(n)

# Test case
print("Factorial of 50:", factorial(50))
