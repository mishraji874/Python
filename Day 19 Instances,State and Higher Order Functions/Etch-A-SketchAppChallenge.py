from turtle import Turtle,Screen

t = Turtle()
screen = Screen()

def forward():
    t.forward(10)

def backward():
    t.backward(10)

def right():
    t.right(60)

def left():
    t.left(60)

def clear():
    t.clear()
    t.home()

screen.listen()
screen.onkey(key="W", fun=forward)
screen.onkey(key="S", fun=backward)
screen.onkey(key="A", fun=left)
screen.onkey(key="D", fun=right)
screen.onkey(key="C", fun=clear)
screen.exitonclick()