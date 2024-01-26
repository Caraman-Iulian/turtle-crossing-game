import turtle as t
from turtle_class import Player
from scoreboard_class import ScoreBoard, GameOver
from obstacle_class import Obstacle
import time
screen = t.Screen()
t.colormode(255)
screen.screensize(600, 600)
screen.listen()
screen.tracer(0)
player = Player()
scoreboard = ScoreBoard()
obstacle = Obstacle()
player.creating_player()
scoreboard.create_scoreboard()
screen.onkeypress(player.moving_forward, 'w')
the_statement = True
while the_statement == True:
    time.sleep(0.1)
    screen.update()
    obstacle.create_obstacle()
    obstacle.move_obstacles()
    for i in obstacle.emptylist:
        if player.playerlist[0].distance(i.pos()) < 15:
            gameover = GameOver()
            gameover.finish()
            the_statement = False
    if player.playerlist[0].ycor() > 310:
        player.at_finish_line()
        scoreboard.update_scoreboard()
        scoreboard.print_scoreboard()
        obstacle.level_up()



screen.exitonclick()
