"""Write a function analyse_dna(sequence) that defines an inner function gc_content()
to calculate GC% . The outer function should print whether the given DNA is AT rich
or GC rich sequence."""

sequence = input("Enter a DNA sequence: ").upper()
def analyse_dna(sequence):
    def gc_content():
        sequence_length = len(sequence)
        if sequence_length == 0:
            return 0
        gc_count = sequence.count('G') + sequence.count('C')
        return (gc_count / sequence_length) * 100
    gc = gc_content()
    print("DNA sequence:", sequence)
    print("GC content:", round(gc, 2), "%")
    if gc > 50:
        print("GC-rich sequence")
    elif gc < 50:
        print("AT-rich sequence")
    else:
        print("Equal AT and GC content")
analyse_dna(sequence)

#analyse_dna() is the outer function.
#gc_content() is the inner function that calculates the GC percentage.
#sequence.count('G') counts guanine bases.
#sequence.count('C') counts cytosine bases.
#If GC content exceeds 50%, the sequence is classified as GC-rich.
#If GC content is below 50%, it is classified as AT-rich.
