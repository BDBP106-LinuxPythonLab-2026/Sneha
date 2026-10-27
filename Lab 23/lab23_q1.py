import matops
a=[1,2,3]
b=[4,5,6]
A=[[1,2],[3,4]]
v=[5,6]
B=[[5,6],[7,8]]

print("Dot product:",matops.dot_product(a,b))
print("Matrix_vector product:",matops.matrix_vector(A,v))
print("Matrix_matrix product:",matops.matrix_matrix(A,B))
print("Cross product:",matops.cross_product(a,b))