import Tkinter as tk
from glob import glob
import os
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time
import escapeFunctions
import subprocess
import serial
import os
from datetime import datetime
from datetime import timedelta
from pirc522 import RFID
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=1)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



class ImageDisplay(tk.Tk):
    def __init__(self, **kwargs):
        tk.Tk.__init__(self, **kwargs)
        #self.geometry('2000x2000')
	self.attributes("-fullscreen", True) 
        self.wm_attributes('-type', 'splash') # no title bar
        self.attributes('-zoomed', True) # fullscreen
        self.window = tk.Label(self, bg='black')
        self.window.pack(fill=tk.BOTH, expand=True)

        # preload all images
        self.cache = {"pic.png":""}
        for filename in glob('/home/pi/Pictures/*.png'):
            _, name = os.path.split(filename)
            img = Image.open(filename).resize((1920, 1080))
            self.cache[name] = ImageTk.PhotoImage(img)
        # ~ print(self.cache) #  debug: uncomment to print all loaded images
        self.current = '' # keep track of currently loaded image

    def load_image(self, *args):
        # generate filename from sensor data
        # eg load_image(0, 1, 1, 0) = "pic23.png"
        filename = "pic" + "".join(str(i) for i, x in enumerate(args, 1) if x) + ".png"
        if filename != self.current:
            self.window.config(image=self.cache[filename])
            self.current = filename
            self.window.update()

display = ImageDisplay()

while True:
    sensor1 = GPIO.input(32)
    sensor2 = GPIO.input(36)
    sensor3 = GPIO.input(38)
    sensor4 = GPIO.input(40)

    display.load_image(sensor1, sensor2, sensor3, sensor4)

    if sensor1 and sensor2 and sensor4 and not sensor3:
        print("you fucking did it!")
        GPIO.output(12, 1)
        time.sleep(10)
        GPIO.output(12, 0)
        display.load_image() # clear the display
    #else:
        #time.sleep(5)