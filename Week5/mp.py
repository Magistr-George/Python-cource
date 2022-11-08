# implementation of card game - Memory

import simplegui
import random

turns = 0
state = 0
first_index, second_index = 0, 0

# helper function to initialize globals
def new_game():
    global cards, turns, list_res, list_bool  
    turns = 0
    list_res = []
    list_bool = [False] *16    
    
    iter_list = [[], []]
    for lst in range(len(iter_list)):
        iter_list[lst] = range(0,8)
        random.shuffle(iter_list[lst])        
        list_res += iter_list[lst]
    
# define event handlers
def mouseclick(pos):
    global state, turns, first_index, second_index, list_bool
    index = pos[0]/50

    # add game state logic here
    if not list_bool[index]:
        list_bool[index] = True
        if state == 0:
            state = 1
            first_index = index
            turns += 1
        elif state == 1:
            second_index = index
            state = 2
        else:
            state = 1
            if list_res[first_index] != list_res[second_index]:
                list_bool[first_index] = False
                list_bool[second_index] = False            
            first_index = index
            turns += 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global turns
    label.set_text("Turns = " + str(turns))
    
    for i in range(len(list_res)):
        #print str(cards_val[i])
        if list_bool[i] == True:
             canvas.draw_text(str(list_res[i]), (50*i+10, 60), 40, "White")
        else:
            canvas.draw_polygon([(i*50, 0), (i*50, 100),(i*50+50, 100),(i*50+50, 0)],4, "White", "Green") 

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()