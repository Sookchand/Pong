import time
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Initialize the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create the line
line = turtle.Turtle()
line.speed(0)
line.color("white")
line.penup()
line.goto(0, -300)
line.setheading(90)

for _ in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)
line.hideturtle()

# Create paddles and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Bind keyboard events to paddle movements
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Game loop
game_on = True
while game_on:
    time.sleep(ball.move_speed)  # Adjust the sleep time for the game speed
    screen.update()
    ball.move()

    # Check for collisions with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Check for collisions with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Check for r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Check for l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Exit the game when the game is over
screen.exitonclick()
