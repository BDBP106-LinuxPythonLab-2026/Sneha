fin=open('stringmatrix.dat','r')
grid=[]
for i in fin:
    row=i.split()
    grid.append(row)
fin.close()
print(grid)

columns=[]
for i in range(0,len(grid[0])):
    col=[]
    for j in range(0,len(grid)):
        col.append(grid[j][i])
    columns.append(col)
print(columns)

diagonals=[]
rows=len(grid)
columns=len(grid[0])
for k in range(rows+columns-1):
    d=[]
    for i in range(rows):
        j=k-i
        if j>=0 and j<columns:
            d.append(grid[i][j])
    diagonals.append(d)
print(diagonals)
