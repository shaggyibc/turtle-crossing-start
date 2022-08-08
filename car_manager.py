from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2.5



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        new_car = Turtle()
        new_car.speed("slow")
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randrange(-250, 260, 40))
        new_car.setheading(180)
        self.car_list.append(new_car)

    def move_car(self):
        for cars in self.car_list:
            cars.forward(self.car_speed)

    def add_cars(self):
        make_car = 1
        if make_car == random.randint(1, 5):
            self.create_car()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
