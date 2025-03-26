from turtle import Turtle, Screen

screen = Screen()

class Player(Turtle):
    def __init__(self, height):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.height = height
        self.starting_position()


    def up(self):
        self.forward(20)

    def starting_position(self):
        self.goto(0, -(self.height / 2 - 20))
        self.setheading(90)


