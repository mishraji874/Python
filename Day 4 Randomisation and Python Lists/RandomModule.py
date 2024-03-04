import random

random_integer = random.randint(1, 10) #it is saying that the integer is starting from 1 to 10
print(random_integer)

random_float = random.random() # it always print the number from 0 to any number which is less than 1 but never include 1 in it
print(random_float)

random_float = random.random() * 5
print(random_float)


love_score = random.randint(1,100)
print(f"Your love score is {love_score}")