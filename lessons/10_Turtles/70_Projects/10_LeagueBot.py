""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.addshape('lessons/10_Turtles/images/leaguebot_bolt.gif')

t = turtle.Turtle()
t.shape('lessons/10_Turtles/images/leaguebot_bolt.gif')
t.shapesize(10, 10)
t.pencolor('blue')

# Draw hexagon
sides = 6
angle = 360 / sides
distance = 100

for _ in range(sides):
    t.forward(distance)
    t.right(angle)

screen.mainloop()