def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper

@log_function_call
def analyse_dna(sequence):
    def gc_content():
        total = len(sequence)
        if total == 0:
            return 0
        g_count = sequence.upper().count('G')
        c_count = sequence.upper().count('C')
        return (g_count + c_count) / total * 100
    gc = gc_content()
    print("GC Content:", round(gc, 2), "%")
    if gc > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")
    return gc

# Test case
result = analyse_dna("ATGCGCGCAT")
print("Returned GC percentage:", result)

