# Q1) Import numpy and check the version
import numpy as np
print("Q1) Numpy version: " ,np.__version__)
print()

print("Q2)")# Q2
# (i) Create a 1D array from 0 to 9.
arr=np.arange(10)
print("(i) 1D array: ", arr)
print()

# Create a boolean array of size 3×3.
arr=np.ones((3,3),dtype=bool)
print("(ii) Boolean array: ")
print(arr)
print()

# (iii) Create an array of prime numbers from 1 to 50.
arr=np.arange(1,51)
prime=arr[np.array([all(i%j!=0 for j in range(2,int(i**0.5)+1))and i>1 for i in arr])]
print("(iii) Prime numbers: ",prime)
print()

# (iv) Create a 1D array with 20 random elements and reshape it into a 4×5 array. Print both arrays.
arr=np.random.randint(1,100,20)
print("(iv) 1D array: ")
print(arr)
arr2=arr.reshape(4,5)
print("4X5 array:")
print(arr2)
print()

# (v) Create two 1D arrays a and b. Array a contains numbers from 0 to 9, and b contains only 1s. Stack them horizontally.
a=np.arange(10)
b=np.ones(10,dtype=int)
arr=np.hstack((a,b))
print("(v) Array a: ",a)
print("Array b: ",b)
print("Horizontally stacked array: ",arr)
print()

# (vi) Find the intersection of two arrays.
a=np.arange(1,101)
b=np.array([i for i in range(2,600) if all (i%j!=0 for j in range(2,int(i**0.5)+1))][:100])
arr=np.intersect1d(a,b)
print("(vi) Array a: ",a)
print("Array b: ",b)
print("Intersection of two array: ",arr)
print()

# (vii) Remove the elements from array a that are present in array b.
a=np.arange(1,101)
b=np.array([i for i in range(2, 600) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))][:100])
arr=np.setdiff1d(a,b)
print("(vii) Array a: ",a)
print("Array b: ",b)
print("Differece (a-b): ",arr)
print()

# (viii) Obtain the indices of common elements between two arrays.
a = np.arange(1, 101)
b = np.array([i for i in range(2, 600)if all(i % j != 0 for j in range(2, int(i**0.5) + 1))][:100])
indices = np.where(a == b)
print("(viii) Array a:", a)
print("Array b:", b)
print("Common element indices:", indices)
print()

print("ix") # (ix) Extract elements of array a that are greater than 5 and less than 20.
a = np.arange(1, 101)
arr = a[(a > 5) & (a < 20)]
print("Original Array:", a)
print("Elements greater than 5 and less than 20:")
print(arr)