import Tkinter as tk
import RPi.GPIO as GPIO
import time
import escapeFunctions
import subprocess
import serial
import os
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
while n==1:

    try:


        sensor1 = GPIO.input(32)
        sensor2 = GPIO.input(36)
        sensor3 = GPIO.input(38)
        sensor4 = GPIO.input(40)
        if sensor1 or sensor2 or sensor3 or sensor4:
            time.sleep(.2)
            sensor1 = GPIO.input(32)
            sensor2 = GPIO.input(36)
            sensor3 = GPIO.input(38)
            sensor4 = GPIO.input(40)
            print(sensor1)
            print(sensor2)
            print(sensor3)
            print(sensor4)

            if sensor1 and sensor2 and sensor3 and sensor4:
                if sensorCase != 1:  # only enter the image open function if status is different than previous status
                    try:
                        image.kill()
                    except:
                        x=1
                    #image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic1.png"])
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic1234.png"])

                    time.sleep(5)

                    sensorCase = 1
            elif sensor1 and sensor2 and sensor3 and not sensor4:
                if sensorCase != 2:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic123.png"])
                    time.sleep(5)
                    sensorCase = 2
            elif sensor1 and sensor2 and sensor4 and not sensor3:
                if sensorCase != 3:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/correct.png"])

                    print("you did it!")
                    GPIO.output(12, 0)
                    time.sleep(10)
                    GPIO.output(12, 1)
                    image.kill()


                    sensorCase = 3
            elif sensor1 and sensor3 and sensor4 and not sensor2:
                if sensorCase != 4:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic134.png"])
                    time.sleep(5)
                    sensorCase = 4
            elif sensor2 and sensor3 and sensor4 and not sensor1:
                if sensorCase != 5:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic234.png"])
                    time.sleep(5)
                    sensorCase = 5
            elif sensor1 and sensor2 and not sensor3 and not sensor3:
                if sensorCase != 6:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic12.png"])
                    print("sensorcase: ")
                    sensorCase = 6
                    #print(sensorCase)
                    time.sleep(5)
            elif sensor1 and sensor3 and not sensor2 and not sensor4:
                if sensorCase != 7:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic13.png"])
                    time.sleep(5)
                    sensorCase = 7
            elif sensor1 and sensor4 and not sensor2 and not sensor3:
                if sensorCase != 8:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic14.png"])
                    time.sleep(5)
                    sensorCase = 8
            elif sensor2 and sensor3 and not sensor1 and not sensor4:
                if sensorCase != 9:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic23.png"])
                    time.sleep(5)
                    sensorCase = 9
            elif sensor2 and sensor4 and not sensor1 and not sensor3:
                if sensorCase != 10:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic24.png"])
                    time.sleep(5)
                    sensorCase = 10
            elif sensor3 and sensor4 and not sensor1 and not sensor2:
                if sensorCase != 11:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic34.png"])
                    time.sleep(5)
                    sensorCase = 11
            elif sensor1 and not sensor2 and not sensor3 and not sensor4:
                if sensorCase != 12:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic1.png"])
                    time.sleep(5)
                    sensorCase = 12
            elif sensor2 and not sensor1 and not sensor3 and not sensor4:
                if sensorCase != 13:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic2.png"])
                    time.sleep(5)
                    sensorCase = 13
            elif sensor3 and not sensor1 and not sensor2 and not sensor4:
                if sensorCase != 14:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic3.png"])
                    time.sleep(5)
                    sensorCase = 14
            elif sensor4 and not sensor1 and not sensor2 and not sensor3:
                if sensorCase != 15:
                    try:
                        image.kill()
                    except:
                        x = 1
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/pic4.png"])
                    time.sleep(5)
                    sensorCase = 15

            else:
                if sensorCase != 17:
                    try:
                        image.kill()
                    except:
                        x = 1
                    #add different image to show error message
                    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-Z", "-F","-q","/home/pi/Pictures/snowman.png"])
                    sensorCase = 17

        elif not sensor1 and not sensor2 and not sensor3 and not sensor4:
            if sensorCase != 16:
                try:
                    image.kill()
                except:
                    x = 1

            sensorCase = 0

    except KeyboardInterrupt:
        print("keyboard interrupted")
#while n==1:
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