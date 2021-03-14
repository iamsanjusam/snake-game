from turtle import Turtle

FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.print_scores()

    def print_scores(self):
        self.write(arg=f"Score: {self.score - 1}", move=False, align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", move=False, align='center', font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_scores()