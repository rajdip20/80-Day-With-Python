# Draw a Square

from turtle import Screen, Turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "green")


for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


screen = Screen()
screen.exitonclick()
