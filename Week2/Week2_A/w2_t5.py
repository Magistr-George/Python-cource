# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

import simplegui 

message = "My second frame!"

# Handler for mouse click
def click():
    print message

frame = simplegui.create_frame("My second frame", 100, 200)
frame.add_button("Click me", click)

frame.start()

