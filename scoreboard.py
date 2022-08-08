FONT = ("Courier", 24, "normal")
from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("black")
        self.penup()
        self.shapesize(stretch_len=20, stretch_wid=1)
        self.speed("fastest")
        self.goto(-200, 250)
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()