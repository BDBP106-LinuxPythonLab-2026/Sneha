# Write a script to check if a given number, N, is prime or not

N = int(input("Enter a positive integer: "))
if N > 1:
    for i in range(2, N):
        if N % i == 0:
            print("Not prime")
            break # stops the for loop as soon as Python finds a number that divides N evenly.
    else:
        print("Prime num") # prints "Prime number" if the loop finishes without encountering break.
else:
    print("Not Prime") # executes when N > 1 is False, meaning the number is less than or equal to 1.
