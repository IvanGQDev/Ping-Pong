from turtle import Turtle
FONT = ("Cascadia Code", 20, "normal")

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,150)
        self.score = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.write(arg=f"Score:{self.score}                 Score:{self.score2}",align="center",font=FONT)
        self.hideturtle()

    def increment_score_p1(self):
            self.clear()
            self.score += 1
            self.write(arg=f"Score:{self.score}                 Score:{self.score2}",align="center",font=FONT)

    def increment_score_p2(self):
            self.clear()
            self.score2 += 1
            self.write(arg=f"Score:{self.score}                 Score:{self.score2}",align="center",font=FONT)
