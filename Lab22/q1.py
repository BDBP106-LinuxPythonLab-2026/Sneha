def greet_decorator(func):
    def wrapper():
        print("Hello, world!")
        func()
        print("Goodbye, world!")
    return wrapper
@greet_decorator
def message():
    print("This is my first attempt as using decorator.")
message()
