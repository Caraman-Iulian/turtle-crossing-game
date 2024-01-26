import turtle as t

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(500)
        self.goto(-320, 260)
        self.color('black')
        self.score = 0
        self.hideturtle()
    def create_scoreboard(self):
        self.write(f'Level: {self.score}', False, font=('Courier', 27, 'normal'))


    def update_scoreboard(self):
        self.score += 1
        self.clear()
    def print_scoreboard(self):
        self.write(f'Level: {self.score}', False, font=('Courier', 27, 'normal'))

class GameOver(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
    def finish(self):
        self.write('Game Over', False, align= 'center', font=('Courier', 40, 'normal'))