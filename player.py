from turtle import Turtle

class Player:
    def __init__(self, color = "", player=0):
        self.blocks = []
        self.color = color
        if player == 1:
            self.create_player1()
        elif player == 2:
            self.create_player2()

    def create_player1(self):
        n = -20
        for i in range(3):
            new_block = Turtle("square") 
            new_block.color(self.color)
            new_block.penup()
            new_block.goto(-290,n)
            n += 20
            self.blocks.append(new_block)

    def create_player2(self):
        n = -20
        for i in range(3):
            new_block = Turtle("square") 
            new_block.color(self.color)
            new_block.penup()
            new_block.goto(290,n)
            n += 20
            self.blocks.append(new_block)

    def move_up(self):
        if self.blocks[2].ycor() < 220:
            self.blocks[0]
            self.blocks[0].setheading(90)
            self.blocks[0].forward(20)
            self.blocks[1]
            self.blocks[1].setheading(90)
            self.blocks[1].forward(20)
            self.blocks[2]
            self.blocks[2].setheading(90)
            self.blocks[2].forward(20)
    
    def move_down(self):
        if self.blocks[0].ycor() > -220:
            self.blocks[0]
            self.blocks[0].setheading(270)
            self.blocks[0].forward(20)
            self.blocks[1]
            self.blocks[1].setheading(270)
            self.blocks[1].forward(20)
            self.blocks[2]
            self.blocks[2].setheading(270)
            self.blocks[2].forward(20)