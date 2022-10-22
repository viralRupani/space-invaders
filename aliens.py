import time
from turtle import Turtle
import random

MOVE_DISTANCE_SPEED = 10


class Aliens:
    def __init__(self):
        self.all_aliens = []

    def create_alien(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_alien = Turtle()
            new_alien.penup()
            # new_alien.color(self.color)
            new_alien.shape('square')
            new_alien.shapesize(2, 1)
            new_alien.goto(random.randint(-320, 320), 300)
            self.all_aliens.append(new_alien)

    def move_on(self):
        for alien in self.all_aliens:
            print(MOVE_DISTANCE_SPEED)
            move_forward = alien.ycor() - MOVE_DISTANCE_SPEED
            alien.goto(alien.xcor(), move_forward)

    def increase_speed(self):
        global MOVE_DISTANCE_SPEED
        MOVE_DISTANCE_SPEED = 20
