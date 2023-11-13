from turtle import Turtle

MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.goto(0, 0)
        self.color("white")
        self.penup()
        self.dx = 10  # Initialize dx
        self.dy = 10  # Initialize dy
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.setx(new_x)
        self.sety(new_y)

    def bounce_y(self):
        # Reverse the y velocity of the ball
        self.dy *= -1

    def bounce_x(self):
        # Reverse the x velocity of the ball
        self.dx *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
