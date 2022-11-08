import simplegui

attempts = 0  		
successful_attempts = 0
width = 200
height = 200
clock = 0			
msec = 0			
stop_clock = False	

def format(time):
    global msec
    
    msec = time % 10
    sec = (time / 10) % 60
    minute = (time / 10) / 60
    
    if sec < 10:
        return str(minute) + ":0" + str(sec) + "." + str(msec)
    else:
        return str(minute) + ":" + str(sec) + "." + str(msec)

def start():
    global stop_clock
    
    if stop_clock == False:
        timer.start()
        stop_clock = True

def stop():
    global attempts, successful_attempts, stop_clock
    
    if stop_clock == True:
        timer.stop()
        stop_clock = False
        
        attempts += 1
        if msec == 0:
            successful_attempts += 1

def reset():
    global attempts, successful_attempts, clock, msec, stop_clock
    
    if stop_clock == True:
        timer.stop()
        stop_clock = False
    
    attempts = 0
    successful_attempts = 0
    clock = 0
    msec = 0

def tick():
    global clock
    
    clock += 1
    if clock - clock // 1000 * 1000 == 600:
        clock += 400

# define draw handler
def draw(canvas):
    canvas.draw_text(str(successful_attempts)+ "/" + str(attempts), [160, 20], 20, "Green")
    canvas.draw_text(format(clock),[65, 110], 28, "White")

# create frame and timer
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
timer = simplegui.create_timer(100, tick)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100) 
frame.set_draw_handler(draw)

# start frame
frame.start()