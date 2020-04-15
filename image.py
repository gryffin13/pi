#!/usr/bin/env python

from glob import glob
from PIL import Image, ImageTk
import os

PICTURES = 'pictures' # folder where the original pictures are kept
DEBUG = False

def get_images(screensize, force_resize=False):
    """
    get images of the proper size to fit the screen
    if those do not exist, get the original size images and resize them
    :screensize: a 2-tuple of width, height, or tk instance
    """
    try:
        width = screensize.winfo_screenwidth()
        height = screensize.winfo_screenheight()
        screensize = width, height
    except AttributeError:
        pass

    sized_dirname = os.path.join(PICTURES, 'x'.join(map(str, screensize)))
    if not os.path.exists(sized_dirname):
        os.mkdir(sized_dirname)

    cache = {"pic.png":""}
    for filename in glob(os.path.join(PICTURES, '*.png')):
        _, name = os.path.split(filename)
        sized_path = os.path.join(sized_dirname, name)
        if os.path.exists(sized_path) and not force_resize:
            img = Image.open(sized_path)
            if DEBUG: print('load presized:', sized_path)
        else:
            img = Image.open(filename).resize(screensize)
            img.save(sized_path)
            if DEBUG: print('load and resize original:', filename)

        cache[name] = ImageTk.PhotoImage(img)
    return cache

# test
if __name__ == "__main__":
    DEBUG = True
    import Tkinter as tk # photoimage requires an active tkinter window
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenwidth()
    print(get_images(root))
    # ~ print(get_images((600,400)))
