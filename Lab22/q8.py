"""Write a function analyse_dna(sequence) that defines an inner function gc_content()
to calculate GC% . The outer function should print whether the given DNA is AT rich
or GC rich sequence. (copy this code from Lab 21 to Lab 22 folder)"""

def analyse_dna(sequence):
    def gc_content():
        g_count=sequence.upper().count('G')
        c_count=sequence.upper().count('C')
        total=len(sequence)
        if total==0:
            return 0
        return(g_count+c_count)/total*100
    gc=gc_content()
    print("GC content:",round(gc,2),"%")
    if gc>50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")

# Test case
analyse_dna("ATGCGCGCAT")
