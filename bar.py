from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        y = self.ycor() + 50
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 50
        self.goto(self.xcor(), y)
