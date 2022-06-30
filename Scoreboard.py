from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()
    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"GAME OVER! \n Final Score: {self.score}", align=ALIGNMENT, font=FONT)
