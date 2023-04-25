import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

loop = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Turtler")
screen.tracer(0)

player1 = Player()
scoreboard1 = Scoreboard()

# Used to create new cars
cars = []

screen.listen()
screen.onkey(fun=player1.move, key="Up")


# Spawns a new car every 6th iteration through the loop
game_is_on = True
while game_is_on:
    if loop % 6 == 0:
        random_color = random.randint(0, 5)
        start_x = random.randint(300, 450)
        start_y = random.randint(-230, 230)
        new_car = CarManager(random_color, start_x, start_y)
        cars.append(new_car)
    time.sleep(0.1)
    screen.update()
    if player1.finish_line():
        scoreboard1.increase_level()
        car.increase_car_speed()
        player1.increase_move_distance()

    for car in cars:
        if player1.distance(car) < 25:
            game_is_on = False
            scoreboard1.game_over()
            time.sleep(5)

    player1.finish_line()
    new_car.move_left()
    for car in cars:
        car.move_left()

    # Only spawn a new car on every multiple of 6
    loop += 1
