student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#Looping thorugh dictionaries
for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

#Loop through a data frame
for (key, value) in student_dataframe.items():
    print(value)

#loop through rows of a data frame
for (index, row) in student_dataframe.iterrows():
    print(index)
    print(row)
    print(row.student)