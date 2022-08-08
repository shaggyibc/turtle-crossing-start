from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.speed("fastest")
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.left(90)

    def turtle_move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False
