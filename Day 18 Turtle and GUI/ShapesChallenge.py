from turtle import Turtle, Screen
import random
t = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat","SlateGray", "SeaGreen"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()