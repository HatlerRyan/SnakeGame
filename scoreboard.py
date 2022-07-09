from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.high_score = 0
        self.re_score()

    def add_point(self):
        self.score += 1

    def re_score(self):
        self.clear()
        # self.reset()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.re_score()