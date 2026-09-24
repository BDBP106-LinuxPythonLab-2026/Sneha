N=int(input("Enter a positive integer: "))
isPrime = True
i=2
while i <= N:
    if N % i == 0:
        isPrime = False
        break
if isPrime:
    print("Prime")
else:
    print("Not prime")
