import Tkinter as tk
import RPi.GPIO as GPIO
import time
import escapeFunctions
import subprocess
import serial
import os
from PIL import Image, ImageTk
from glob import glob

from datetime import datetime
from datetime import timedelta
from pirc522 import RFID
uid1 = [61,186,177,115,69] #blue tag #1
uid2 = [174,17,68,32,219] # white tag #1
uid3 = [27,146,74,13,206] #blue tag #2
uid4 = [3,46,57,27,15] #white tag #2
uid5=[218,254,123,30,65] #green
uid6=[234,46,223,30,5] #gray
uid7=[218,207,9,30,2] #white
uid8=[234,15,56,30,195] #black
uid9=[234,133,144,23,232]#red
uid10=[218,186,237,30,147]#yellow
uid11=[218,143,18,30,89]#purple
uid12=[218, 79, 26, 30, 145]#green #2
orderList = [uid1[4],uid3[4],uid5[4],uid6[4],uid7[4],uid8[4],uid9[4],uid10[4],uid11[4],uid8[4],uid9[4],uid12[4]]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=1)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#dash dot dash dot   dash dash dash   dash dot   dash dash dot   dot dash dot   dot dash   dash   dot dot dot
morse=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
morse=['null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null']

start_time = datetime.now()

startHour = start_time.hour
startMin = start_time.minute
startSec = start_time.second


sensor1 = False
sensor2 = False
sensor3 = False
sensor4 = False
sensorCase=0
picPath = " /home/pi/Pictures/"
poorly = ("/home/pi/Videos/poorly.mp4")
wisely = ("/home/pi/Videos/Wisely2.m4v")
rdr = RFID()
i=0
n=1
q=1
j=0
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

while n==1:
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
    (error, tag_type) = rdr.request()
    if not error:
        (error, uid) = rdr.anticoll()
        if not error:
            print("UID: " + str(uid))
            if uid[4] == orderList[i]:
                print("match")
                i=i+1
                escapeFunctions.playVideoFun(wisely, "A")
                time.sleep(5)
                if i==12:
                    image = subprocess.Popen(
                        ["feh", "--hide-pointer", "-x", "-Z", "-F", "-q", "/home/pi/Pictures/finalSnowman.png"])
                    time.sleep(20)
                    image.kill()
                    #GPIO.output(8,1)
                    n=0
            else:
                print("wrong")
                #n=0
                i=0
                escapeFunctions.playVideoFun(poorly, "A")
                time.sleep(5)

while q==1:

    dot = GPIO.input(35)
    dash = GPIO.input(37)
    #print(morse)
    if dot==1:
	time.sleep(.07)
	while GPIO.input(35)==1:
		time.sleep(.01)
        print("dot")
        if j<=20:
            morse[j]='dot'
            #time.sleep(.25)
            j=j+1
        elif j>20:
            del morse[0]
            morse.append('dot')
            #time.sleep(.25)
    if dash==1:
	time.sleep(.07)
	while GPIO.input(37)==1:
		time.sleep(.01)
        print("dash")
        if j <= 20:
            morse[j]='dash'
            #time.sleep(.25)
            j = j + 1
        elif j>20:
            del morse[0]
            morse.append('dash')
            #time.sleep(.25)
    #if morse == ['dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash','dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash', 'dash']:
    if morse==['dash','dot','dash','dot','dash','dash','dash','dash','dot','dash','dash','dot','dot','dash','dot','dot','dash','dash','dot','dot','dot']:
        print("you win")
        try:
            image.kill()
        except:
            x = 1

        image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F", "-q", "/home/pi/Pictures/FINAL.png"])
        time.sleep(25)
        now = datetime.now()
        nowHour = now.hour
        nowMin = now.minute
        nowSec = now.second
        dtHour = now.hour - start_time.hour
        dtMin = now.minute - start_time.minute
        dtSec = now.second - start_time.second

        print("final time:")
        print(dtHour),
        print(":"),
        print(dtMin),
        print(":"),
        print(dtSec),
        q=0

        print("Open your final box. Code: 22-28-9")
        print("CONGRATS!!!!!")


        #store final time