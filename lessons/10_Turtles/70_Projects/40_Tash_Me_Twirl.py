
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here

import turtle

""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustache (youre welcome i fixed it.)
3) Move the moustache to the right spot on the emoji (once again, youre welcome.)

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Change the background image
screen.bgpic("/workspaces/Python-Apprentice-new/lessons/10_Turtles/images/sanic_64.png")

# Create the turtle and change its shape to a moustache
tash = turtle.Turtle()
tash.shape("arrow")  # Change to moustache shape if available
tash.shapesize(stretch_wid=2, stretch_len=3)
tash.color("black")

# Move the moustache to the right spot on the emoji
tash.penup()
tash.goto(0, 50)  # Adjust coordinates to position on emoji face
tash.pendown()

# do the thing

def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    tash.penup()

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    tash.goto(x, y)
  
screen.onclick(screen_clicked)

def tashclick(x, y):
    tash.right(360)

tash.onclick(tashclick)

# Keep the window open
turtle.done()
