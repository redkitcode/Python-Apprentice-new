"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
# crazy? i was crazy once. they locked me in a room. a rubber room. a rubber room with rats. and rats make me crazy! 

import turtle

turtle.setup(600,600,0,0) # i think im losing my mind. numbers make no sense. what is 0? is it everything? is it nothing? what is the concept of void? is it reality? does it even exist? is there a reason why we use 0 for everything? think about it... 10. 0. 01. see? it does so much but then again it does almost nothing. how the heck did someone even create this idea and think, "hm, yeah that makes sense to me."
window = turtle.Screen()

t = turtle.Turtle() # seriously though im confused. am i losing braincells or gaining them by thinking deep thoughts? and of all things, why 0? it could have been about something useful like world hunger or something, but nooo. my brain has other plans. im going to curl up in a ball and implode (just like my braincells or lack thereof.)



# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.
# ok then whatever floats your boat! boats are nice. they ship stuff. they float. they are expensive. they have a manufactureraror and their manufactureraror has money. money is awesome. money is currency. i had some once, then it just walked away from me. not very nice of it. i sure hope it enjoys its new bank account. bank accounts usually have debit or credit cards attached to them. whats your debit/credit card number? mines 1234 5678 7543 and the cvv is 210. oops, shouldnt have told you that. unless youre a bank worker. if you are, then ive been having lots of trouble with my account and i was hacked by a russian dude named "vladmir putin". he said he knows where i live. he said it was right next to boring middle school in boring oregon. the fool really thought my ip was 0.999.888.777. i mean come on, everyone knows that ip addresses are made of 4 numbers, and each number is between 0 and 255. besides, my real ip is 0.816.3264. so glad i was using the sponsor of todays video, nordvpn. nordvpn is a virtual private network that encrypts your- ok ok just kidding. but seriously, use a vpn if you want to torrent. or if youre scared of russian spies gaining access to your location. or if you arent. im kidding. oifiysgkihlrso8gfursuoiflyrwhosfuyauhofioeifheriofrk

def make_a_shape(t):
    """make a shape ya dang turtle."""    
    ...

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = 40 # wait... 0? oh no. here we go again. is nothing everything? is everything nothing? im not sure but i *do* remember that one commercial for a medicine that went "nothing is everythaayayaaayang ooh whoa whoa" so iconic. anyways, 0. again. that reminds me of the movie quote "its poop again." why does that remind me of 0, you may ask? well you see, o looks similar to 0, a western arabic numeral derived from ancient or something times. that turns it into leetspeak. "its p00p again." remove the ps. "its 00 again." you see? everything is 0. 0 is nothing and yet it can turn a number like 1 into 10. or 01, but thats not the point. the point is that being nothing is wonderful. thats what somebody called me once. i should probably thank him. thank you whoever you were. you made me the man i am today. a crazy guy. so truly i must say once more, thank you. thank you for awakening me to the enigma that is void. thank you for showing me who i truly am on the inside. if it werent for you, i wouldnt have been able to notice how without nothing, doing an action would not be possible. creating wouldnt be possible. not is a wonderful concept similar to infinity. it is a concept that shows that even a nobody can become somebody. although, nobody is technically somebody given my philosophy on it, but whatever, you know what i mean. um, where was i again? oh right, coding. coding is tricky, but rewarding. just like living, or the concept of 0. see? see? everything is 0! anyways, back to coding. we need to create shapes. i like shapes. the number 0 has a shape. im out of shape. you can shape clay. you can turn it into the number 0. or you can put it back in the ground if you dont find a use for it. whatever suits you. so uh shapes! yeahhhh! woooo! shapes! go shapes! go shapes! go shapes! shapes are wonderful. shapes. you can eat one if its made of chocolate. or solid nitrogen. i heard you can do that if you use liquid nitrogen but im no chemist so dont take my word for it. or googles word for it, larry page isnt a chemist. dang it i forgot i was coding. well back to coding (for real this time!)

for i in range(num_shapes):
    make_a_shape(t)
    t.right(360/num_shapes)
