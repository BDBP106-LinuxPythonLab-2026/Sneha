principal = float(input("Enter principal: "))
rate = float(input("Enter rate of interest (% per annum): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100
amount = principal + simple_interest

print("Simple Interest:", simple_interest)
print("Amount:", amount)
