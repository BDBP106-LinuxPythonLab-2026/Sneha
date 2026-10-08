#Convert lists to sets to remove duplicates
#print students taking both courses
#print students taking only Python
#print students taking exactly one course
#print every unique student, sorted alphabetically
#ask for student name and print name and the course(s) that the student is enrolled in

python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]

python_students = set(python_class)
java_students = set(java_class)

both = python_students & java_students
print("Students taking both courses:", both)

only_python = python_students - java_students
print("Students taking only Python:", only_python)

exactly_one = python_students ^ java_students
print("Students taking exactly one course:", exactly_one)

all_students = python_students | java_students
print("Every unique student:", sorted(all_students))

name = input("Enter student name: ")

if name in python_students and name in java_students:
    print(name, "is enrolled in both Python and Java.")
elif name in python_students:
    print(name, "is enrolled in Python only.")
elif name in java_students:
    print(name, "is enrolled in Java only.")
else:
    print(name, "is not a student enrolled in either Python or Java.")
