"""Write a decorator called count_calls that counts how many times a function is called
and prints the count. Use the template code below and fill in the correct piece of code."""

def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        func()
        print(f"Call count: {count}")
    return wrapper

@count_calls
def say_hi():
    print("Hi!")
say_hi()
say_hi()
say_hi()
