S = input("Enter a string: ")
half = len(S)//2  # floor division discards the fractional part for this positive result.
first_half = S[:half] # The start index is omitted, so Python starts from index 0 till the index before the half 
print("First half of string:" ,first_half)
