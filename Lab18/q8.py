#Write a program to interchange the even and odd components of an input list. The list can contain any type of variables.
my_list = [23, 32, 33, 44, 'BDBH101', 'hello', 'python', 15, 1e-10, True, 'hit']
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)
