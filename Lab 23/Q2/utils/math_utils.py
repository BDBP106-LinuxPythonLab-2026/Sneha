# math_utils.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None
    return a / b


def remainder(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None
    return a % b
