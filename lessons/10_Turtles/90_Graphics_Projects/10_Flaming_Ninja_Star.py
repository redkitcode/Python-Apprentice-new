"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup(600,600,0,0)               # Set the size of the window
window = turtle.Screen()

baseSize = 10  # the size of the black part of the star
flameSize = 0  # the length of the flaming arms
turn = 25 # i forgor what this does but it looks important so i wont make it implode and incinerate it using the power of the sun itself. so yeah thats why i have this goofy goober of a variable here :p

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

# do more actions with the simulated drawing turtle that is surprisingly fast and a very intricate artist i must say. anywho yeah the thing will commit a thing. what is that thing you may ask? tax evasion. no, im serious. the turtle is actually a mastermind at not paying for things. even mr krabs is afraid of it is how cheap the turtle is. ever since it was a kid, it hated paying for things. it torrented on a regular basis. and now the turtle refuses to pay its debt to the government. its very clever, that turtle. never got caught. pretty impressive, huh? anyways the turtle is smart and can produce the most valid art when it comes to mathematics. too bad the turtle uses its powers for crime. what a shame. hope it gets caught. where was i? oh right, coding...

for i in range(1000):

    for i in range(50):
        t.pencolor(getRandomColor())

        t.fillcolor(getRandomColor()) 
   
        t.begin_fill()

        t.left(turn*2)

        t.forward(turn) 

        turn+=5

        t.end_fill()

    t.right(turn)



t.hideturtle() 

turtle.done() 
