import re

dna = "ATCGCGAATTCAC"
pattern = r"GG[AT]CC"

if re.search(pattern, dna):
    print("AvaII restriction site found.")
else:
    print("AvaII restriction site not found.")
