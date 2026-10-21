 """A DNA sequence encodes each amino acid making up a protein as a three-nucleotide
 sequence called a codon. For example, the sequence fragment AGTCTTATATCT contains
 the codons AGT, CTT, ATA, TCT if read from the first position. If read from
 the second position, it yields the codons GTC, TTA, TAT and if read from the third
 position we get TCT, TAT, ATC. Write a function to extract the codons into a list of
 3-letter strings given a sequence and from what position (input as an integer) the 
 sequence should be read. As an example, output the 3-letter strings from the sequence
 GTTTCGATTATAACG read from the (i) 1st position and (ii) 3rd position."""



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
