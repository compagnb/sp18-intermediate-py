import turtle
import player

wn = turtle.Screen()
wn.bgcolor("red")

playerImg = "saucer.gif"
wn.register_shape(playerImg)

player = player.Player(playerImg)

## wn.onkey(functionName, "key")
wn.onkey(player.goLeft, "Left")
wn.onkey(player.goRight, "Right")
wn.onkey(player.speedUpSlowPoke, "Up")
wn.onkey(player.slowYourRoll, "Down")

while True:
            player.move()
