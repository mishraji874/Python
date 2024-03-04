student_heights = input("Input a list of students heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
result = (sum(student_heights)/len(student_heights))
print(result)
print(round(result))