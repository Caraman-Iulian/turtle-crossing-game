import turtle as t
from random import randint, choice
# screen = t.Screen()
colors =['red', 'blue', 'black', 'brown', 'purple', 'wheat']

class Obstacle:
    def __init__(self):
        self.emptylist = []
        self.carspeed = 10
    def create_obstacle(self):
        random_chance = randint(1, 4)
        if random_chance == 1:
            new_obstacle = t.Turtle('square')
            new_obstacle.shapesize(stretch_wid=1, stretch_len=2)
            new_obstacle.penup()
            new_obstacle.color(choice(colors))
            new_obstacle.setheading(180)
            y = randint(-285, 285)
            new_obstacle.goto(330, y)
            self.emptylist.append(new_obstacle)

    def move_obstacles(self):
        for obstacle in self.emptylist:
            obstacle.forward(self.carspeed)

    def level_up(self):
        self.carspeed += 10








