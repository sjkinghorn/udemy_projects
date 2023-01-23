from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    car_manager.add_car(frequency=.2)
    car_manager.move_cars()

    # Detect collision with car.
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    #  Detect finishline.
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.level_up()
        car_manager.increase_speed()

screen.exitonclick()
