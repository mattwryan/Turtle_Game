from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

    def increase_move_distance(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += 10


