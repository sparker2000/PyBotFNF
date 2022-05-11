from PIL import ImageGrab
from pynput.keyboard import Controller

keyboard = Controller()

# Calculates the distance between two colors.  
# If the distance is less than or equal to the tolerance, it returns true.
# (x-x1)^2 + (y-y1)^2 + (z-z1)^2 <= tol^2
pixel_tolerance = 15
def is_close(x, y, z, x1, y1, z1):
    return (x-x1)**2 + (y-y1)**2 + (z-z1)**2 <= pixel_tolerance**2

# Takes a screen capture of the game arrows and returns a PIL image.
def screen_cap_arrows():
    left = 995
    top = 155
    width = 335
    height = 80
    printscreen_pil = ImageGrab.grab((left,top,left+width,top+height))

    return printscreen_pil

# Checks the left arrow for any expected color changes.
# Presses 'a' if it finds a match.
def check_left(pil):
    left = 32
    top = 37

    leftPixel = pil.getpixel((left, top))
    if(is_close(leftPixel[0], leftPixel[1], leftPixel[2], 194, 75, 153) 
    or is_close(leftPixel[0], leftPixel[1], leftPixel[2], 170, 110, 161)):
        keyboard.press('a')
    else:
        keyboard.release('a')

# Checks the up arrow for any expected color changes.
# Presses 'w' if it finds a match.
def check_up(pil):
    left = 210
    top = 20

    upPixel = pil.getpixel((left, top))
    if (is_close(upPixel[0], upPixel[1], upPixel[2], 18, 250, 5) or
    is_close(upPixel[0], upPixel[1], upPixel[2], 65, 215, 72)):
        keyboard.press('w')
    else:
        keyboard.release('w')

# Checks the down arrow for any expected color changes.
# Presses 's' if it finds a match.
def check_down(pil):
    left = 123
    top = 50

    downPixel = pil.getpixel((left, top))
    if(is_close(downPixel[0], downPixel[1], downPixel[2], 0, 255, 255) or
    is_close(downPixel[0], downPixel[1], downPixel[2], 54, 218, 222)):
        keyboard.press('s')
    else:
        keyboard.release('s')

# Checks the right arrow for any expected color changes.
# Presses 'd' if it finds a match.
def check_right(pil):
    left = 285
    top = 40

    rightPixel = pil.getpixel((left, top))    
    if(is_close(rightPixel[0], rightPixel[1], rightPixel[2], 249, 57, 63) or 
    is_close(rightPixel[0], rightPixel[1], rightPixel[2], 203, 99, 107)):
        keyboard.press('d')
    else:
        keyboard.release('d')

# Very simple method to determine if program should end.  If it sees a black pixel, it will end.
# ToDo: this only accounts for game loss.  Need to also account for game win. 
def should_kill(pil):
    left = 305
    top = 34
    
    return pil.getpixel((left, top)) == (0, 0, 0)

# Main loop.  Will run until the game is over.
def pixel_loop():
    arrow_pil = screen_cap_arrows()

    check_left(arrow_pil)
    check_right(arrow_pil)
    check_up(arrow_pil)
    check_down(arrow_pil)

    return should_kill(arrow_pil)

while True:
    if pixel_loop():
        break