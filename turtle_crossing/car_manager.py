from turtle import Turtle
import random
COLORS = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self, frequency):
        if random.random() < frequency:
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            random_ycor = (random.randint(-250, 250))
            car.goto(300, random_ycor)
            car.setheading(180)
            self.cars.append(car)
        else:
            pass

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
