import turtle as t

class Player(t.Turtle):
    def __init__(self):
        self.playerlist = []
    def creating_player(self):
        new_player = t.Turtle('turtle')
        new_player.penup()
        new_player.goto(0, -300)

        new_player.speed(200)
        new_player.shapesize(1.1)
        new_player.setheading(90)
        new_player.color('black')

        self.playerlist.append(new_player)


    def moving_forward(self):
        self.playerlist[0].forward(25)



    def at_finish_line(self):
        if self.playerlist[0].ycor() > 280:
            self.playerlist[0].goto(0, -300)





