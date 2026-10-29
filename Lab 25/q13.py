import re

dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"

pattern = r"[^ATGC]+"

# Split wherever one or more non-standard bases occur
result = re.split(pattern, dna)

# Remove empty strings, if any
result = [part for part in result if part]

print(result)
