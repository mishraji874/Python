"""
KEY             VALUE
Bug             An error in a program that prevents the program from running as expected.
Function        A piece of code that you can easily call over and over again.
Loop            The action of doing something over and over again.
"""

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Debugging"] = "Degubbing is used to debug the program. It tells the each and every step of the program in which way the code is working."
print(programming_dictionary["Debugging"])

#Create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#edit an existing item
programming_dictionary['Bug'] = "A worth on computer."
print(programming_dictionary["Bug"])

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])