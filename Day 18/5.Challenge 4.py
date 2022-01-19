# Generate a random walk

from turtle import Screen, Turtle
import random
import turtle

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)
directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

Screen().exitonclick()
