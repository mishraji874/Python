from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
t.shape("turtle")
t.speed("fastest")
directions = [0, 90, 180, 270]

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

def circle(num_of_gap):
    for i in range(int(360/num_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.right(num_of_gap)

circle(20)
screen.exitonclick()