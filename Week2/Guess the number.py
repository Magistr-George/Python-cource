# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# helper function to start and restart the game
def new_game(): 
    # initialize global variables used in your code here
    global min_number, max_number, computer_choice, count
    count = 0
    min_number = 0
    input_guess    

# define event handlers for control panel
def range100():
    global computer_choice, count, max_number
    print "New game, range is from 0 to 100"
    max_number = 99
    count = 7
    computer_choice = random.randint(min_number,max_number)   
    input_guess

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global computer_choice, count
    print "New game, range is from 0 to 1000"
    max_number = 999
    count = 10
    computer_choice = random.randint(min_number,max_number)    
    input_guess
    
def input_guess(guess):
    global count
    guess = int(guess)
    
    if count > 0:
        count -= 1
        print("Guess was " + str(guess))
        print("Number of remaining guesses is " + str(count))
        if guess > computer_choice:
            print "Lower!"
        elif guess < computer_choice:
            print "Higher!"
        else:
            print "Correct!"
            range100()
    else: 
        print "Out of guesses"
        range100()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess ", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
frame.start
