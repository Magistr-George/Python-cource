# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def time():
    pass

def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons   
def counter_start():
    global timer
    timer = simplegui.create_timer(1000, tick)
    timer.start()
    
def counter_stop():
    timer.stop()
    
def counter_reset():
    global counter
    counter = 0

        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start", counter_start, 100)
frame.add_button("Stop", counter_stop, 100)
frame.add_button("Reset", counter_reset, 100)
timer = simplegui.create_timer(1000, time)

# Start timer
timer.start()
