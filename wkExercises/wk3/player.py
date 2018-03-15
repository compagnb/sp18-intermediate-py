## Player Module
## player should move, attack/collide, turn, take user input
import turtle
from random import randint

class Player(turtle.Turtle):
            def __init__(self, img):
                        turtle.Turtle.__init__(self)
                        self.penup()
                        self.speed(0)
                        self.shape(img)
                        self.color("blue")
                        self.vel = 1
                        self.maxVel = 10

            def move(self):
                        self.forward(self.vel)

            def goRight(self):
                        self.right(30)

            def goLeft(self):
                        self.left(30)

            def speedUpSlowPoke(self):
                        if self.vel < self.maxVel:
                                    self.vel = self.vel + 1

            def slowYourRoll(self):
                        if self.vel > self.maxVel *-1:
                                    self.vel = self.vel - 1

            def ckBorders(self):
                if self.xcor() > 195 or self.xcor() < -195:
                        self.right(180)

                if self.ycor() > 195 or self.ycor() <- 195:
                        self.right(180)









                    
