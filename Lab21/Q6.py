"""Calculate ATP yield using an inner function"""

def cell_metabolism(glucose, oxygen):
    def energy_output():
        glucose_used = min(glucose, oxygen // 6)
        return glucose_used * 38
    return energy_output()
atp = cell_metabolism(glucose, oxygen)
glucose = int(input("Enter the number of glucose molecules: "))
oxygen = int(input("Enter the number of oxygen molecules: "))
print("Total ATP produced:", atp)
