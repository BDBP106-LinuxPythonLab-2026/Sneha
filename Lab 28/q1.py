# 1) Analysis of the thrL gene

from Bio.Seq import Seq

thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")

# 1. Length
print("Length:", len(thrL))

# 2. GC content
gc = (thrL.count("G") + thrL.count("C")) / len(thrL) * 100
print("GC content:", round(gc, 2), "%")

# 3. Translation
print("Translation:", thrL.translate())
print("Translation without stop:", thrL.translate(to_stop=True))

# 4. Count ACC occurrences
print("Number of ACC occurrences:", str(thrL).count("ACC"))

# 5. Last codon
print("Last codon:", thrL[-3:])

# 6. First 12 bases of reverse complement
print("Reverse complement (first 12 bases):",
      thrL.reverse_complement()[:12])