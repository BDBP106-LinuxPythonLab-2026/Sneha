import re

dna = "ATCGCGYAATTCAC"

# Find all characters that are not A, T, G, or C
ambiguous_bases = re.findall(r"[^ATGC]", dna)

if ambiguous_bases:
    print("Ambiguous bases found:", ambiguous_bases)

    # Extract all unambiguous bases
    non_ambiguous_bases = re.findall(r"[ATGC]", dna)

    print("Non-ambiguous bases:", "".join(non_ambiguous_bases))

else:
    print("No ambiguous bases found.")
    print("The DNA sequence contains only A, T, G, and C.")
