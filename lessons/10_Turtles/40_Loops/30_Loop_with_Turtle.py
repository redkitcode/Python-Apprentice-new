
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

angle = 360 / 5                            # Angle to turn for a pentagon

for i in range(5):
    tina.shape('turtle')                    # Set the shape of the turtle to a turtle
    tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

    tina.forward(100)                       # Move tina forward by the forward distance
    tina.left(angle)                        # Turn tina left by the left turn


turtle.exitonclick()      # Close the window when we click on it
