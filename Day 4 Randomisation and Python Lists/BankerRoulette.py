# how to use the spilt function
import random

name_string = input("Give me everybody's names, seperated by a coma. ")
names = name_string.split(", ")
print(names)
#get the number of items in the list
print(len(names))
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
print(random_choice)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")