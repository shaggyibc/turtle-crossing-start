import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
sleep_time = .1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
car = CarManager()
scoreboard = Scoreboard()


# player_int = screen.textinput(prompt="Enter players initials", title="Turtle game")

screen.listen()
screen.onkey(key="Up", fun=timmy.turtle_move)

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    car.add_cars()
    car.move_car()

    # Detect Collisions:
    for cars in car.car_list:
        if timmy.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False

# Detect a crossing
    if timmy.is_at_finish():
        timmy.goto(0, -280)
        scoreboard.increase_score()
        car.level_up()






screen.exitonclick()