import turtle
from turtle import Turtle

MOVE_DISTANCE_SPEED = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 2)
        self.goto(0, -200)

    def move_left(self):
        if self.xcor() != -320:
            left_x_core = self.xcor() - MOVE_DISTANCE_SPEED
            self.goto(left_x_core, self.ycor())
            # print(self.xcor())

    def move_right(self):
        if self.xcor() != 320:
            right_x_core = self.xcor() + MOVE_DISTANCE_SPEED
            self.goto(right_x_core, self.ycor())