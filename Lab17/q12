# Write a program to subtract two matrices, m1 and m2, using a list of lists.

m1 = [[1, 2, 3],             # Define two matrices
      [4, 5, 6],
      [7, 8, 9]]

m2 = [[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]

m3 = []                      # Create an empty list to store the result

for i in range(len(m1)):     # Iterate through each row of m1
    row = []                 # Create an empty list for the current row

    for j in range(len(m1[i])):             # Iterate through each element of the row
        row.append(m1[i][j] - m2[i][j])     # Subtract corresponding elements of m2 from m1

    m3.append(row)           # Add the completed row to the result matrix

print(m3)
