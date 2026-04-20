"""
Pentagon Crazy

This program already works. Run it, then change it to make it draw a different pattern.
"""

import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600, startx=0, starty=0)

colors = ("red", "blue", "green", "yellow", "orange")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)
myTurtle.width(1)
myTurtle.speed(999)

sides = 10 # i like 0. 0. 0. 0. but you know what i like more? 8. 8, 8, 8 is great. you can turn it this way you can turn it that way its still 8, 8, 8 is great, i forgot the rest. and yes that was indeed a sesame street reference. i know i know, i was born in the early 2010s, but i still know tons of older media. cry about it

for i in range(1080):
    if i == 100:
        myTurtle.width(2)
    if i == 200:
        myTurtle.width(3)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i/10)
    myTurtle.right(360/sides + 5)

myTurtle.hideturtle()

turtle.done()
