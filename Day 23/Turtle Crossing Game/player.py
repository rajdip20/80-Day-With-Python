from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # def go_down(self):
    #     new_y = self.ycor() - MOVE_DISTANCE
    #     self.goto(self.xcor(), new_y)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    