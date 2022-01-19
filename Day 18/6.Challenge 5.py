# Draw a Spirograph

from turtle import *
import random
import turtle

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)
timmy.speed(0)
angle = 5

for _ in range(72):
    timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.circle(100)
    timmy.setheading(angle)
    angle += 5

Screen().exitonclick()
