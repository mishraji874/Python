from turtle import Turtle, Screen
dashed = Turtle()
for i in range(15):
    dashed.forward(10)
    dashed.penup()
    dashed.forward(10)
    dashed.pendown()

screen = Screen()
screen.exitOnClick()