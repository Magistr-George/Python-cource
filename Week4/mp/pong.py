# Implementation of classic arcade game Pong

#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
min_pos = (BALL_RADIUS+PAD_WIDTH, BALL_RADIUS)
max_pos = (WIDTH-BALL_RADIUS-PAD_WIDTH, HEIGHT-BALL_RADIUS)
bounce_speed = [1.1, 1]

pad_right_pos = pad_left_pos = HEIGHT / 2
pad_right_speed = pad_left_speed = 0
speed = 3

LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel, ball_dir, speed_devisor # these are vectors stored as lists
    speed_devisor = 60
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_dir = [random.choice([-1,1]),random.choice([-1,1])]
    ball_vel = [ball_dir[0] * random.randrange(120, 240), ball_dir[1] * random.randrange(60, 180)]

def update_ball():
    global max_pos, min_pos, ball_dir, speed_devisor

    for i in range(2):
        ball_pos[i] += ball_vel[i] / speed_devisor
        
        if (ball_pos[i] <= min_pos[i]): 
            ball_pos[i] = min_pos[i]
            ball_dir[i] *= (-1)
        elif (ball_pos[i] >= max_pos[i]): 
            ball_pos[i] = max_pos[i]
            ball_dir[i] *= (-1)
        
        if ball_pos[i] in (min_pos[i], max_pos[i]):
            ball_vel[i] *= -ball_dir[i]
            if speed_devisor > 10:
                speed_devisor -= 2
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, scores  # these are ints
    score1, score2 = 0, 0 
    scores = [score1, score2]
    spawn_ball()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    update_ball()
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 3, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    for i in range(2):
        global pad_left_pos, pad_right_pos
        pad_left_pos += pad_left_speed
        pad_right_pos += pad_right_speed
        
        if (pad_left_pos <= HALF_PAD_HEIGHT): 
            pad_left_pos = HALF_PAD_HEIGHT
        elif (pad_left_pos >= HEIGHT-HALF_PAD_HEIGHT): 
            pad_left_pos = HEIGHT-HALF_PAD_HEIGHT
        
        if (pad_right_pos <= HALF_PAD_HEIGHT): 
            pad_right_pos = HALF_PAD_HEIGHT
        elif (pad_right_pos >= HEIGHT-HALF_PAD_HEIGHT): 
            pad_right_pos = HEIGHT-HALF_PAD_HEIGHT
            
    # draw paddles
    canvas.draw_line((HALF_PAD_WIDTH, pad_left_pos - HALF_PAD_HEIGHT), 
                     (HALF_PAD_WIDTH, pad_left_pos + HALF_PAD_HEIGHT),
                     PAD_WIDTH, 'Yellow')  
    canvas.draw_line((WIDTH-HALF_PAD_WIDTH, pad_right_pos - HALF_PAD_HEIGHT), 
                     (WIDTH-HALF_PAD_WIDTH, pad_right_pos + HALF_PAD_HEIGHT),
                     PAD_WIDTH, 'Blue')
    
    # determine whether paddle and ball collide
    if ball_pos[0] == min_pos[0]:
        if not (pad_left_pos + HALF_PAD_HEIGHT >= ball_pos[1] >= pad_left_pos - HALF_PAD_HEIGHT):
            score(1)
    elif ball_pos[0] == max_pos[0]:
        if not (pad_right_pos + HALF_PAD_HEIGHT >= ball_pos[1] >= pad_right_pos - HALF_PAD_HEIGHT):
            score(0)
            
    # draw scores
    canvas.draw_text(str(scores[0]), (WIDTH*0.2, HEIGHT*0.2), HEIGHT*0.2, 'white')
    canvas.draw_text(str(scores[1]), (WIDTH*0.7, HEIGHT*0.2), HEIGHT*0.2, 'white')

def score(player):
    global ball_dir
    scores[player] += 1
    ball_dir = [player * 2 - 1,random.choice([-1,1])]
    spawn_ball()    
    
    
def keydown(key):
    global pad_right_speed, pad_left_speed, speed
    if key == simplegui.KEY_MAP['up']: 
        pad_right_speed = -speed
    elif key == simplegui.KEY_MAP['down']: 
        pad_right_speed = speed
    elif key == simplegui.KEY_MAP['w']: 
        pad_left_speed = -speed
    elif key == simplegui.KEY_MAP['s']: 
        pad_left_speed = speed

def keyup(key):
    global pad_right_speed, pad_left_speed
    if key == simplegui.KEY_MAP['up']: 
        pad_right_speed = max (0, pad_right_speed)
    elif key == simplegui.KEY_MAP['down']: 
        pad_right_speed = min (0, pad_right_speed)
    elif key == simplegui.KEY_MAP['w']: 
        pad_left_speed = max (0, pad_left_speed)
    elif key == simplegui.KEY_MAP['s']: 
        pad_left_speed = min (0, pad_left_speed)


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)

# start frame
new_game()
frame.start()
