"""Write a decorator called check_positive that checks whether the argument passed to
a function is positive. If it is positive, execute the function; otherwise, print
"Number must be positive"."""

def check_positive(func):
    def wrapper(n):
        if n > 0:
            return func(n)
        else:
            print("Number must be positive")
    return wrapper
@check_positive
def display_number(n):
    print("Number is:",n)

# Call the function
display_number(10)
display_number(-5)