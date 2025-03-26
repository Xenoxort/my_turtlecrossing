import math
import random
import turtle as t
from turtle import Turtle

t.colormode(255)

class Cars:
    def __init__(self, width, height):
        self.car_list = []
        self.width = width
        self.height = height
        self.speed = 1
        self.frequency = 30
        self.colortuple = ()


    def create(self):
        if random.randint(1, math.ceil(self.frequency)) == 1:
            self.colortuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(self.colortuple)
            new_car.goto(self.width / 2 + 20, random.randint(int(-(self.height / 2 - 50)), int(self.height / 2 - 50)))

            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.back(self.speed)

    def increase_speed(self):
        self.speed += 0.3
        self.frequency *= 0.9


