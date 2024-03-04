from turtle import Turtle, Screen

square = Turtle()
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)

for i in  range(4):
    square.forward(100)
    square.left(90)


screen = Screen()
screen.exitonclick()