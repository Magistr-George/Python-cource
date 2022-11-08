# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    for w in range(GRID_SIZE):
        for h in range(GRID_SIZE):
            canvas.draw_circle([2 * w * BALL_RADIUS + BALL_RADIUS, 2 * h * BALL_RADIUS + BALL_RADIUS], BALL_RADIUS, 1, "Red", "Red")
                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

