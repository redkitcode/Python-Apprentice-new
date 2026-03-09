"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 


colors = ["#276221", "#3b8132", "#46923c", "#52a447", "#5bb450", "#72bf6a", "#8bca84", "#acd8a7", "#cce7c9"]    # define a list of colors

while True:
    for color in colors:                            # loop through the colors
        tina.pencolor(color)
        tina.pendown()
        tina.fillcolor(color)
        tina.begin_fill()
        for i in range(4):
            tina.forward(200)
            tina.right(90)
        tina.end_fill()

    for i in range(len(colors)):                            # loop through the colors
        color = colors[-1-i]
        tina.pencolor(color)
        tina.pendown()
        tina.fillcolor(color)
        tina.begin_fill()
        for i in range(4):
            tina.forward(200)
            tina.right(90)
        tina.end_fill()


# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here

turtle.exitonclick()                     # Close the window when we click on it