from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        with open("data.txt") as file:
            high_score = file.read()
            self.write(f"Score: {self.score}    High score: {high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        with open("data.txt") as file:
            high_score = int(file.read())
        if self.score > high_score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()
