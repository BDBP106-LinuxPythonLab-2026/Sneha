# Write a script to convert the binary number B into decimal.
B = input("Enter a binary number: ")
decimal = int(B, 2)           # the syntax is: int(string, base)
                              # Here: B is the string containing the number.
                              # 2 specifies that the number is represented in binary (base 2).
                              # int(B, 2) converts that binary representation into a decimal integer.
                              # decimal = stores the result in the variable decimal.
print("Decimal is", decimal)
