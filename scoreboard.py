from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()  # This is to hide the arrow which comes after printing the scoreboard on the screen

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over:(",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear() # This clears the previous texts(The previous score on the screen)
        self.update_scoreboard()
