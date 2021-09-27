from PIL import ImageGrab
from random import randint
import os
import keyboard
import time
try:
    os.chdir("C:\\Users\\Admin")
    os.makedirs("college screensort")
except:
    pass
os.chdir("C:\\Users\\Admin\\college screensort")
while True:
    if keyboard.is_pressed('p'):
        a=ImageGrab.grab()
        b=time.asctime(time.localtime(time.time())).split(" ")
        b=f"{b[0]} {b[1]} {b[2]} {b[len(b)-1]} ".upper()
        a.save(f"{b}{randint(0,10000098)}.png")
        time.sleep(2)
    elif keyboard.is_pressed('s'):
        break