from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("purple")
        self.speed("fastest")
        self.goto(0,0)

    def move(self):
        self.forward(20)

    def move_heading(self, heading):
        self.setheading(heading)
