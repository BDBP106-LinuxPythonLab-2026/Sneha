# 3) Translation of all six reading frames

from Bio.Seq import Seq

mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")

# Reverse complement
rev = mystery.reverse_complement()

# 1. Translate all six reading frames

print("Forward reading frames:")

forward_frames = []

for i in range(3):
    frame = mystery[i:]

    # Trim to multiple of 3
    frame = frame[:len(frame) - len(frame) % 3]

    protein = frame.translate()
    forward_frames.append((i + 1, protein))

    print(f"Frame +{i + 1}:", protein)

print("\nReverse reading frames:")

reverse_frames = []

for i in range(3):
    frame = rev[i:]

    # Trim to multiple of 3
    frame = frame[:len(frame) - len(frame) % 3]

    protein = frame.translate()
    reverse_frames.append((-(i + 1), protein))

    print(f"Frame -{i + 1}:", protein)

# 2. Find the longest ORF

all_frames = forward_frames + reverse_frames

longest_orf = ""
longest_frame = None

for frame_number, protein in all_frames:

    protein = str(protein)

    # Find every start codon (M)
    for i in range(len(protein)):

        if protein[i] == "M":

            # Find the next stop codon
            stop = protein.find("*", i)

            if stop != -1:

                orf = protein[i:stop + 1]

                if len(orf) > len(longest_orf):
                    longest_orf = orf
                    longest_frame = frame_number

print("\nLongest ORF:", longest_orf)
print("Reading frame:", longest_frame)
print("ORF length:", len(longest_orf), "amino acids")