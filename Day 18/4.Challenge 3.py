# Draw different shape

from turtle import Screen, Turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "green")
colours = ["red", "green", "blue", "DarkOrchid", "black", "CornflowerBlue", "SeaGreen", "DeepSkyBlue"]
side = 3

while side <= 10:
    timmy.color(colours[side-3])
    for _ in range(side):
        timmy.forward(100)
        timmy.right(360/side)
    side += 1


screen = Screen()
screen.exitonclick()
