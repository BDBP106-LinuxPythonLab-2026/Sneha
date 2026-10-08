#Ask the user to enter a number 'n'
#Print the numbers from 1 to n as the header row.
#Start from row 1.
#For each row, print the row number.
#Multiply the row number by each number from 1 to n.
#Print each multiplication result in the row.
#Repeat until all n rows are printed.

n=int(input("Enter a number: "))
print("  ".rjust(4), end="")
for i in range(1, n + 1):
    print(f"{i:4}", end="") #f"{i:4}" → print i with a width of 4 #end="" → stay on the same line
print()
for i in range(1, n + 1):
    print(f"{i:4}", end="")

    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")

    print()