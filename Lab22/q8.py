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