from turtle import Turtle, Screen
import random
t = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat","SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
t.pensize(15)
t.speed(6)
for i in range(200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()