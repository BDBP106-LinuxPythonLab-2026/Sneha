def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def nextPrime(n):
    number = n + 1
    while True:
        if is_prime(number):
            return number
        number = number + 1
# Main program
n = int(input("Enter an integer: "))
print("Next prime number =", nextPrime(n))
