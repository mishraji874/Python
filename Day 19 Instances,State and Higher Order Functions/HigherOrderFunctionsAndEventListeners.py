from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key = "space", fun = move_forward) #onkey function is used when we will press the designated key then the certain function will perform its task
screen.exitonclick()

"""
when we are using the in-built functions then try to use the keyword argumnets instead of positional arguments

keyword argumnets

def my_funciton(c = 3, a = 1, b = 2)

positional arguments

def my_function(1, 2, 3)
"""