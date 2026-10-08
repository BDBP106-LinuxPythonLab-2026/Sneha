#input an integer
#print whether it's positive, negative or zero
#if it's non-zero, then print whether it's even or odd
#if integer%15==0 then print Fizzbuzz

n=int(input("Enter an integer: "))
if n>0:
    print("It is a positive integer")
elif n==0:
    print("It is zero")
elif n<0:
    print("It is a negative integer")
if n%2==0:
    print("Even")
else:
    print("Odd")
if n%15==0:
    print("FizzBuzz number")