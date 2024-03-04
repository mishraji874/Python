import turtle as t
from turtle import Screen
import random

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0 ,255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
t.pensize(15)
t.speed(6)
for i in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))

screen.exitonclick()