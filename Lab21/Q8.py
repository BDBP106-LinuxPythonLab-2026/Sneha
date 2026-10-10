"""Write a function protein_energy)temp) with an inner function
calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0)"""

temperature=float(input("Enter the temperature in Kelvin: "))
H=float(input("Enter enthalpy charge: "))
S=float(input("Enter entropy charge: "))
def protein_energy(temperature):
      def calculate_free_energy(enthalpy, entropy):
          return enthalpy - temperature*entropy
      G = calculate_free_energy(H, S)
      print("Free energy change(delta G):", round(G,2))
      if G < 0:
          return "Stable"
      else:
          return "Unstable"
result = protein_energy(temperature)
print("Protein stability:", result)
