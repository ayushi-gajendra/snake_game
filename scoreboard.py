from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.write(arg=f"Score:{self.score}",move=False, align="center")

    def score_calculator(self):
        self.score+=1
