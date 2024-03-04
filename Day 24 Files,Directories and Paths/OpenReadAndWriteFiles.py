"""file = open("my_file.txt")
content = file.read()
print(content)
file.close()"""

"""with open("my_file.txt") as file:
    contents = file.read()
    print(contents)"""

"""with open("my_file.txt", mode="w") as file: #w is used for writing the new text in the file and it deletes all the previous content
    file.write("New text.")"""

with open("my_file.txt", mode="a") as file: #a is used for append purpose i.e. it will write the content on the file but without removing the previous content
    file.write("\nNew text.")

with open("new_file.txt", mode="w") as file:
    file.write("New text.")