from turtle import Screen, Turtle, heading
from player import Player
from ball import Ball
from score import Score_board
import random
import time

def draw_line():
    line = Turtle()
    line.color("white")
    line.penup()
    line.goto(0, 500)
    line.setheading(270)
    line.hideturtle()
    for i in range(0, 80):
        line.forward(10)
        if i % 2 == 0:
            line.penup()
        else:
            line.pendown()


screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

scores = Score_board()
draw_line()


player_1 = Player("red", 1)
player_2 = Player("green", 2)

ball = Ball()
screen.update()

screen.listen()
screen.onkey(player_1.move_up, 'w')
screen.onkey(player_1.move_down, 's')
screen.onkey(player_2.move_up, 'i')
screen.onkey(player_2.move_down, 'k')
game_is_on = True
ball.move_heading(180)
while game_is_on:
    screen.update()
    time.sleep(0.2)
    ball.move()
    
    for block in player_1.blocks:
        if ball.distance(block) < 20:
            if player_1.blocks[0].heading() == 90:
                head = random.randint(0,90)
            else:
                head = random.randint(270, 379)
            ball.move_heading(head)

    for block in player_2.blocks:
        if ball.distance(block) < 20:
            if player_2.blocks[0].heading() == 90:
                head = random.randint(100,180)
            else:
                head = random.randint(190, 260)
            ball.move_heading(head)

    if ball.xcor() > 350 or ball.xcor() < -350:
        if ball.xcor() >= 350:
            ball.goto(0,0)
            head = random.randint(100,260)
            if head < 180:
                head += -100
            else:
                head += 100
            ball.move_heading(head)
            scores.increment_score_p1()
        else:
            ball.goto(0,0)
            head = random.randint(100,260)
            ball.move_heading(head)
            scores.increment_score_p2()

    if ball.ycor() > 220 or ball.ycor() < -220:
        if ball.heading() > 270 and ball.heading() < 360:
            head = random.randint(45,85)
            ball.move_heading(head)
        elif ball.heading() > 180 and ball.heading() < 270:
            head = random.randint(125, 140)
            ball.move_heading(head)
        elif ball.heading() < 90 and ball.heading() > 0:
            head = random.randint(285, 315)
            ball.move_heading(head)
        elif ball.heading() > 90 and ball.heading() < 180:
            head = random.randint(225,265)
            ball.move_heading(head)
            




screen.exitonclick()