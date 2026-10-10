"""Calculate ATP yield using an inner function"""

g = int(input("Enter the number of glucose molecules: "))
o = int(input("Enter the number of oxygen molecules: "))
def cell_metabolism(glucose, oxygen):
    def energy_output():
        glucose_used = min(glucose, oxygen // 6)
        return glucose_used * 38
    return energy_output()
atp = cell_metabolism(g, o)
print("Total ATP produced:", atp)