# Image debugging problem

###################################################
# Student should enter code below

import simplegui

# load test image
test_image = simplegui.load_image("https://woman-project.com/uploads/1366750800/783feb725b36f3.jpg")
test_image_size = [test_image.get_width(), test_image.get_height()]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]

# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      test_image_center, test_image_size)

# create frame and register draw handler    
frame = simplegui.create_frame("Shops", test_image_size[0], test_image_size[1])
frame.set_draw_handler(draw)

# start frame
frame.start()
        
                                       