import turtle
from paddle import *
from aliens import Aliens
from game_over import GameOver
import time


screen = turtle.Screen()
over = GameOver()

screen.tracer(0)
paddle = Paddle()

screen.listen()

turtle.onkey(paddle.move_left, "Left")
turtle.onkey(paddle.move_right, "Right")

aliens = Aliens()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    aliens.create_alien()
    aliens.move_on()
    if len(aliens.all_aliens) > 100:
        print(len(aliens.all_aliens))
        aliens.increase_speed()

    for alien in aliens.all_aliens:
        if int(alien.distance(paddle)) < 25:
            print("Game over")
            over.gameover()
            game_is_on = False


screen.exitonclick()
