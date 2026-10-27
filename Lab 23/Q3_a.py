fout=open("stringmatrix.dat","w")
for i in range(3):
    for j in range(4):
        print(chr(65+i*4+j),end=' ',file=fout)
    print(file=fout)
print("string matrix saved successfully.")
fout.close()