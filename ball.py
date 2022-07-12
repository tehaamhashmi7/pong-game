import random
from turtle import Turtle, Screen
from bar import Paddle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.setheading(random.randint(30, 60))
        self.x_move = 10
        self.y_move = 10
        self.a_speed = 3
        self.speed(self.a_speed)

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def wall_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.y_move *= -1
            x = self.xcor() + self.x_move
            y = self.ycor() + self.y_move
            self.goto(x, y)

    paddle = Paddle()
    paddle.hideturtle()

    def paddle_collision(self, paddle):
        if (self.xcor() > 415 or self.xcor() < -415) and self.distance(paddle) < 50:
            self.x_move *= -1
            x = self.xcor() + self.x_move
            y = self.ycor() + self.y_move
            self.goto(x, y)
            self.a_speed += 1
            self.speed(self.a_speed)

    def reset_position(self):

        screen = Screen()

        self.goto(0, 0)
        self.speed(3)
        self.x_move *= -1




