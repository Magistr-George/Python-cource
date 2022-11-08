# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui

count = 0

# Define event handlers for four buttons
def reset():
    global count
    count = 0
    
def increment():
    global count
    count += 1
    
def decrement():
    global count
    count -= 1
    
def print_count():
    global count
    print count

    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Counter", 200, 200)
frame.add_button("Plus one to count", increment)
frame.add_button("Minus one to count", decrement)
frame.add_button("Reset count", reset)
frame.add_button("Print count", print_count)

# Start the frame animation
frame.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2
