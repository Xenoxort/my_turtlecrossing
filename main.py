from player import Player
from turtle import Screen
from levels import Levels

screen = Screen()

height = 500
width = 600

#Setup
screen.setup(height=height, width=width)
screen.title("Turtle Crossing Game")

screen.tracer(0)
#Setup player
my_player = Player(height)

#Setup level
my_level = Levels(width, height)

screen.update()


#Turtle Movement
screen.listen()

screen.onkey(fun=my_player.up, key = "Up")

# The Game
game_on = True
while game_on:
    # Completing the current level
    if my_player.ycor() > (height / 2 - 20):
        my_player.starting_position()

        # Increase level
        my_level.increase_level()

    screen.update()





screen.exitonclick()
