import time
import random
from player import Player
from turtle import Screen
from cars import Cars
from levels import Levels

screen = Screen()

height = 500
width = 600

#Setup screen
screen.setup(height=height, width=width)
screen.title("Turtle Crossing Game")

screen.tracer(0)
#Setup player
my_player = Player(height)

#Setup cars
my_cars = Cars(width, height)

#Setup level
my_level = Levels(width, height)

screen.update()

#Turtle Movement
screen.listen()

screen.onkey(fun=my_player.up, key = "Up")

# The Game
game_on = True
while game_on:
    # Creating and moving cars
    my_cars.create()
    my_cars.move()

    # Completing the current level
    if my_player.ycor() > (height / 2 - 20):
        # Moving back player to starting position
        my_player.starting_position()

        # Increase the speed of the cars
        my_cars.increase_speed()

        # Increase level
        my_level.increase_level()

    # Game Over when hitting a car
    for car in my_cars.car_list:
        if abs(car.xcor() - my_player.xcor()) < 28 and abs(car.ycor() - my_player.ycor()) < 18:
            game_on = False
            #Write Game Over
            my_level.game_over()

    screen.update()
    time.sleep(0.01)




screen.mainloop()
