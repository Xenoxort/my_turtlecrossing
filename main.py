import time
import random
from player import Player
from turtle import Screen
from cars import Cars

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

screen.update()

#Turtle Movement
screen.listen()

screen.onkey(fun=my_player.up, key = "Up")

car_list = []
# The Game
game_on = True
while game_on:
    # Creating and moving cars
    if random.randint(1, 30) == 30:
        tim = my_cars.create()
        car_list.append(tim)
    for car in car_list:
        my_cars.move(car)

    # Completing the current level
    if my_player.ycor() > (height / 2 - 20):
        # Moving back player to starting position
        my_player.starting_position()

        # Increase the speed of the cars
        my_cars.increase_speed() #as the cars get faster the frequency gets lower because the rate of spawning the cars is constant.


    screen.update()
    time.sleep(0.01)




screen.exitonclick()
