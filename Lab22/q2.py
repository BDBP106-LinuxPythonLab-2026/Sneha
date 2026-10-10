"""create this decorator called before_after that
prints "Function is starting...." before the function call and prints "Function has finished!"
after the execution."""

def before_after(func):
    def wrapper():
        print("Function is starting....")
        func()
        print("Function is finished!")
    return wrapper
@before_after
def calculate():
    print("Calculating...")
calculate()
