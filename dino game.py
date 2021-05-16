import turtle
import math
import time
import random

wn = turtle.Screen()
wn.setup(750,400)
turtle.addshape("background.gif")
wn.bgpic("background.gif")


GROUND_LEVEL = -50

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
'''pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("black")
pen.penup()'''

pen.goto(-400, GROUND_LEVEL)
pen.goto(400, GROUND_LEVEL)
pen.penup()

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        turtle.addshape("player.gif")
        self.shape("player.gif")
        self.speed(0)
        self.width = 20
        self.height = 20
        self.dy = 0
        self.dx = 0
        self.state = "ready"
        self.goto(-200,GROUND_LEVEL + self.height/2)
    def jump(self):
        if self.state == "ready":
            self.dy = 12
            self.state = "jumping"
            
class Plant(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color("green")
        self.setposition(300,-40)
        self.shape("square")
        self.setheading(180)
    def move(self):
        self.forward(5)
        
'''class cloud(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.setposition(random.randint(0,300),100)
        turtle.addshape("cloud.gif")
        self.shape("cloud.gif")
        self.setheading(180)
    def move(self):
        self.forward(2)'''
        

class gameover(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        turtle.addshape("screen.gif")
        self.shape("screen.gif")
        self.setposition(0,0)
    def if_lose(self):
        self.showturtle()
        time.sleep(0.5)
        self.hideturtle()
        

    
def isCollision_food_player(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30:
        return True
    else:
        return False
    

player = Player()
plant = Plant()
'''cloud = cloud()'''
a = gameover()
turtle.listen()
turtle.onkey(player.jump,"space")

GRAVITY = -0.8

while True:
    plant.move()
    #cloud.move()
    if isCollision_food_player(plant,player):
        turtle.addshape("playerdead.gif")
        player.shape("playerdead.gif")
        plant.forward(0)
        time.sleep(0.25)
        plant.hideturtle()
        plant.goto(300,-40)
        a.if_lose()
        player.shape("player.gif")
        plant.showturtle()
        
    if plant.xcor()<= -400:
        plant.hideturtle()
        plant.goto(300,-40)
        plant.showturtle()
        
    '''if cloud.xcor()<= -400:
        cloud.hideturtle()
        cloud.goto(random.randint(0,300),100)
        cloud.showturtle()'''
        
    player.dy += GRAVITY
    
    y = player.ycor()
    y += player.dy
    player.sety(y)
    
    if player.ycor() < GROUND_LEVEL + player.height / 2:
        player.sety(GROUND_LEVEL + player.height / 2)
        player.dy = 0
        player.state = "ready"
        
wn.update()





        
        
        

