def get_codons(sequence, position):
    # Convert position to Python index
    start = position - 1
    codons = []
    for i in range(start, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        codons.append(codon)
    return codons
sequence = "GTTTCGATTATAACG"
print("From 1st position:")
print(get_codons(sequence, 1))
print("From 3rd position:")
print(get_codons(sequence, 3))
