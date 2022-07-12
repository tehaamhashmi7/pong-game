import time

from bar import Paddle
from turtle import Turtle, Screen
from ball import Ball
from Score import Scoreboard

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Tehaam's Pong Gaem")

border = Turtle()
border.penup()
border.speed("fastest")
border.hideturtle()
border.goto(0, 300)
border.color("white")
border.setheading(270)


while border.ycor() > -310:
    border.pendown()
    border.forward(10)
    border.penup()
    border.forward(10)


paddle_r = Paddle()
paddle_l = Paddle()

paddle_r.goto(420, 0)
paddle_l.goto(-420, 0)

bounce = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

game_is_on = True

while game_is_on:
    bounce.move()
    bounce.wall_collision()
    bounce.paddle_collision(paddle_r)
    bounce.paddle_collision(paddle_l)
    time.sleep(0.009)

    if bounce.xcor() > 450:
        bounce.reset_position()
        score.score_l()

    if bounce.xcor() < -450:
        bounce.reset_position()
        score.score_r()

screen.exitonclick()
