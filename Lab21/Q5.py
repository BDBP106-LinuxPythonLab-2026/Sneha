"""program to find the sum of all the elements in a list using lambda and reduce
functions"""

from functools import reduce
numbers = [10, 20, 30, 40, 50]
total = reduce(lambda x, y: x + y, numbers)
print("List:", numbers)
print("Sum:", total)