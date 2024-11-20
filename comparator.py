# Code partially taken from https://github.com/shreydan/global-color-picker/blob/main/picker.py

import pynput
from PIL import Image, ImageGrab

old_luminosity = None

def get_luminosity(x,y):
    bbox = (x,y,x+1,y+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    luminosity = 0.299*r + 0.587*g + 0.114*b
    return luminosity

def handle_click(x, y):
    global old_luminosity
    luminosity = get_luminosity(x, y)
    if old_luminosity is None:
        luminosity = old_luminosity
    else:
        print(f"old - new = {old_luminosity - luminosity}")
        old_luminosity = None

def main():
    with pynput.mouse.Events(suppress=True) as events:
        for event in events:
            if isinstance(event, pynput.mouse.Events.Click) and event.pressed:
                handle_click(event.x, event.y)

main()
