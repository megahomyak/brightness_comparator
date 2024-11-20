# Code partially taken from https://github.com/shreydan/global-color-picker/blob/main/picker.py

import pynput
from PIL import Image, ImageGrab
import tkinter
import threading

old_luminosity = None
root = tkinter.Tk()
root.overrideredirect(True)  # Remove window decorations
root.attributes('-alpha', 0.0)  # Make the window invisible
root.attributes('-topmost', 1)  # Keep it on top
threading.Thread(target=root.mainloop).start()


def get_luminosity(x,y):
    bbox = (x,y,x+1,y+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    luminosity = 0.299*r + 0.587*g + 0.114*b
    return luminosity

def on_click(x, y, button, is_pressed):
    global old_luminosity
    root.geometry(f"1x1+{x}+{y}")
    print(x, y)
    if is_pressed:
        luminosity = get_luminosity(x, y)
        if old_luminosity is None:
            luminosity = old_luminosity
        else:
            print(f"old - new = {old_luminosity - luminosity}")
            old_luminosity = None

def on_press(key):
    if key == pynput.keyboard.Key.esc:
        return False

with \
    pynput.mouse.Listener(on_click=on_click) as mouse_listener, \
    pynput.keyboard.Listener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()
