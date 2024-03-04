student_scores = input("Input a list of students scores: ").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(f"The highest score in the class is {max(student_scores)}")