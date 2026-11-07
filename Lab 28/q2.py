# 2) Working with FASTA files

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# 1. Read FASTA file into a list
genes = list(SeqIO.parse("lab_genes.fasta", "fasta"))

print("Number of records:", len(genes))


# 2. Print table of ID, length, GC content and protein

print("\nID\t\tLength\tGC %\tProtein")

for record in genes:
    gc = gc_fraction(record.seq) * 100

    protein = record.seq.translate(to_stop=True)

    print(f"{record.id}\t{len(record.seq)}\t"
          f"{gc:.1f}\t{protein}")


# 3. Write genes with GC content >= 50%

high_gc = [
    record for record in genes
    if gc_fraction(record.seq) * 100 >= 50
]

SeqIO.write(high_gc, "lab high gc.fasta", "fasta")

print("\nNumber of high GC genes:", len(high_gc))


# 4. Sort IDs from highest to lowest GC content

sorted_genes = sorted(
    genes,
    key=lambda record: gc_fraction(record.seq),
    reverse=True
)

print("\nGenes sorted by GC content (highest to lowest):")

for record in sorted_genes:
    print(record.id, gc_fraction(record.seq) * 100)