from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Levels(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-(width/2 - 70), (height/2 - 40))
        self.update_level()


    def update_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)




