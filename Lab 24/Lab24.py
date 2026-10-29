class DNASequence:
    def __init__(self, seq_id, sequence):
        self.seq_id = seq_id
        self.sequence = "".join(sequence.split()).upper()
        self.cleaned_seq = self.sequence
        self.counts = {}

    def complement(self):
        mapping = {"A": "T", "T": "A", "G": "C", "C": "G"}
        comp_seq = ""

        for base in self.sequence:
            comp_seq += mapping[base]

        return DNASequence(self.seq_id + "_comp", comp_seq)

    def reverse_complement(self):
        return DNASequence(
            self.seq_id + "_recomp",
            self.complement().sequence[::-1]
        )

    def transcribe(self):
        rna_seq = self.sequence.replace("T", "U")
        return rna_seq

    def find_site(self, site):
        site = site.upper()
        positions = []
        start = 0

        while True:
            position = self.sequence.find(site, start)

            if position == -1:
                break

            positions.append(position + 1)
            start = position + 1

        return positions


# Test code
s2 = DNASequence("seq2", "ATGGAATTCAG")

print("Original:", s2.sequence)
print("Complement:", s2.complement().sequence)
print("Reverse Complement:", s2.reverse_complement().sequence)
print("mRNA:", s2.transcribe())
print("GAATTC at:", s2.find_site("GAATTC"))
print("TTT at:", s2.find_site("TTT"))