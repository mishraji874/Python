import another_module
print(another_module.another_variable)

"""import turtle
timmy = turtle.Turtle()""" #if we import turtle then we have to write like this to create the object

from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()