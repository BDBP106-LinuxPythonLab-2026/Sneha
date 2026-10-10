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