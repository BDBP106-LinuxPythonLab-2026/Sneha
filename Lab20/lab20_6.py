#Store the student names and marks in a list of tuples.
#Print each student's letter grade (A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F).
#print the class average and the top and bottom scorers.
#Find the top and bottom scorers with a loop, not with max() and a key.


#Create a variable to store the total marks.
#Set the first student as the initial top scorer and bottom scorer.
#Use a for loop to go through each student.
#Unpack the student's name and score from the tuple.
#Check the score and assign the correct letter grade.
#Print the student's name, score, and grade.
#Add the score to the total marks.
#Compare the score with the top score and update if it is higher.
#Compare the score with the bottom score and update if it is lower.
#Calculate the class average.
#Print the class average.
#Print the top scorer and their score.
#Print the bottom scorer and their score.

students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total = 0

top_name, top_score = students[0]                         # Start with the first student as top and bottom
bottom_name, bottom_score = students[0]

for name, score in students:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(name, "-", score, "-", grade)

    total += score                                        # Add score for average

    if score>top_score:                                 # Find top scorer
        top_name=name
        top_score=score

    if score<bottom_score:                             # Find bottom scorer
        bottom_name=name
        bottom_score=score

average = total / len(students)                         # Calculate average
print("Class average:", average)

print("Top scorer:", top_name, "-", top_score)
print("Bottom scorer:", bottom_name, "-", bottom_score)