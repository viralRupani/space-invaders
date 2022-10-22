import turtle


class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def gameover(self):
        self.write("Game Over!", align="center", font=("Courier", 24, "normal"))
