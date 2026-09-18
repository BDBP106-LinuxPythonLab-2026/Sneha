f0 = 0
f1 = 1

print("Fibonacci numbers from f0 to f25:")

for i in range(26):
    print(f"f{i} = {f0}")

    # Swap/update the numbers
    f0, f1 = f1, f0 + f1
