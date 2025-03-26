import random
import turtle as t
from turtle import Turtle

t.colormode(255)

class Cars:
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = 1
        self.frequency = 25


    def create(self):
        self.colortuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.tim = Turtle()
        self.tim.shape("square")
        self.tim.shapesize(stretch_wid=1, stretch_len=2)
        self.tim.penup()
        self.tim.color(self.colortuple)
        self.tim.goto(self.width / 2 + 20, random.randint(int(-(self.height / 2 - 50)), int(self.height / 2 - 50)))

        return self.tim

    def move(self, car):
        car.back(self.speed)

    def increase_speed(self):
        self.speed *= 1.2
        self.frequency *= 0.9


