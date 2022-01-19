# Draw a dashed line

from turtle import Screen, Turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "green")


for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
