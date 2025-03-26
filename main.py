from turtle import Turtle, Screen

screen = Screen()

height = 500
width = 600

#Setup
screen.setup(height=height, width=width)
screen.title("Turtle Crossing Game")

screen.tracer(0)
#My Turtle
tim = Turtle(shape="turtle")
tim.color("black")
tim.penup()
tim.goto(0, -(height/2 - 30))
tim.setheading(90)

screen.update()

#Turtle Movement
screen.listen()

def up():
    tim.forward(20)

screen.onkey(fun=up, key = "Up")


game_on = True
while game_on:

    if tim.ycor() > 230:
        tim.goto(0, -(height / 2 - 30))

    screen.update()





screen.exitonclick()
