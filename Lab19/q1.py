#i
a = [i for i in range(1, 51)]
print(a)

print()
#ii
#a
print(a[1:5])

print()
#b
print(a[3:20:2])

print()
#c
print(a[::2])

print()
#d
print(a[::])

print()
#e
print(a[10::2])

print()
#f
print(a[1:1:1])

print()
#g
print(a[:0:])

print()
#h
print(a[-7::1]) #since its -7 so its counts the last seven in steps of 1

print()
#i
print(a[-6:])

print()
#j
print(a[-10:-4])

print()
#iii
#a
print(a[::-1])

print()
#b
print(a[::-3])

print()
#c
print(a[:1:-2])

print()
#d
print(a[-1:-1:-1])

print()
#e
print(a[:-5:-1])

print()
#f
print(a[:0:-1])

print()
#g
print(a[:-1:-1])

print()
#h
print(a[0:-5:-1])

print()
#i
print(a[-1:5:-1])

print()
#j
print(a[2:2:-1])

print()
#k
print(a[2:1:-1])

print()
#l
print(a[0:-5])

print()
#iii
#a
print(a[1::2])

print()
#b
A= a[:10] + a[35:50:2]
print(A)