"""
POSITiONAL ARGUMENTS

def my_function(a, b, c):
    #do this with a
    #then do this with b
    #finally do this with c

KEYWORD ARGUMENTS

def my_function(a = 1, b = 2, c = 3):
    #do this with a
    #then do this with b
    #finally do this with c
"""
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Angela", "London")
greet_with(location="London", name="Angela")
greet_with(name="Aditya", location="Chennai")