from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self, random_int=random.randint(0, 5), start_x=random.randint(300, 350), start_y=random.randint(-260,
                                                                                                                 260)):
        super().__init__()
        self.shape("square")
        self.color(COLORS[random_int])
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(start_x, start_y)
        self.move_left()

    def move_left(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())

    def spawn_cars(self, car_array):
        for i in range(0, 19):
            new_car = car_array[i]

    def increase_car_speed(self):
        # NOTE: use the global keyword to bring global variables into a function
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
