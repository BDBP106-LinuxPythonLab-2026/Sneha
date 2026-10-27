def dot_product(a,b):
    if len(a)!=len(b):
        print("Error: vectors a and b should be of same size")
        return None
    res=0
    for i in range(len(a)):
        res=res+a[i]*b[i]
    return res

def matrix_vector(A,v):
    if len(A)==0:
        return[]
    for i in range(len(A)):
        if len(A[i])!=len(v):
            print("Matrix column must match vector length")
            return None
    vector=[]
    for i in range(len(A)):
        row=0
        for j in range(len(v)):
            row+=A[i][j]*v[i]
        vector.append(row)
    return(vector)

def matrix_matrix(A,B):
    if len(A)==0 or len(B)==0:
        print("Error:empty matrix")
        return None
    matrix = []
    for i in range(len(A)):
        rowlist = []
        for j in range(len(B[0])):
            res = 0
            for k in range(len(B)):
                res += A[i][k] * B[k][j]
            rowlist.append(res)
        matrix.append(rowlist)
    return(matrix)

def cross_product(a,b):
   if len(a)!=3 or len(b)!=3:
       print("Error:Cross product requires 2 3d vectors")
       return None
   res=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
   return(res)