"""hi
this is a thing that has been created that is currently existing in the universe. it is also an object. did i mention that its a thing? because it is. :D

"""

#import window
import random
import turtle


# give me cooooloooors fancy shmancy dancy in your pantsy. ok fine ill stop.
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

window = turtle
# you should understand this part by now. if you dont, im scared for you.
window.bgcolor("white")

# make le epik tortol
tortol = turtle.Turtle()

# this code does what youd expect obviously
tortol.shape("turtle")

# do the thingy that makes le tortol get zoomies
tortol.speed(0)

# make tortol blue because it could sing im blue dabadee dabadai dabadee dabadai and it would actually apply to it. why is my brain stuck in the early web despite the fact that i wasnt even born yet... ehh who knows maybe because im a 2000s person at heart. so as i was saying, do the thingy yay woohoo.
tortol.color("blue")

# enforce unpaid labor :3 (help im losing it)
for i in range(50):

    # use those fancy shmancy colors i was talking about earlier. wouldnt want it to go to waste right?
    tortol.pencolor(getRandomColor())

    # scooch le tortol. come on, move please. you got this. hey! why are you biting me? ouch! dont do that! somebody get this totrol off of meeeee!
    tortol.forward(9 * i)

    # make le tortol drift even though its not a racecar. well, maybe this tortol is a racecar and im unaware of it...? who knows at this point. oh the unsolved mysteries of life.
    tortol.right(360 / 2+i)

    # make tortol thicc. tortols arent exactly thin you know.
    tortol.width(i)

    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee iiiiiiiiiiiiiiiiiiiiiiiiiiii ooooooooooooooooooooooooo uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu (vowels are important ok?)

turtle.done()