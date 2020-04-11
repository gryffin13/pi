
def playVideoFun (fileName,videoCode):
	import os
	import datetime
	import time
	import RPi.GPIO as GPIO
	time.sleep(.1)
	#state17=GPIO.input(17)
	#state18 = GPIO.input(18)
	if videoCode =="A" or videoCode=="B":
		print("VIDEOCODE CONFIRMED in function")
		print(videoCode)
		print(fileName)
		os.system('omxplayer ' + fileName)
		if videoCode=="B":
			penalty()
		#return

	else:
		print("else happened")
		GPIO.cleanup
		#return
	#print(datetime.datetime.now().time())

	#GPIO.cleanup()
	
	return

def touchPic (sensor1, sensor2, sensor3, sensor4, sensorCase, picPath):
	import os
	import time
	import serial

	#check sensor values
	if sensor1 and sensor2 and sensor3 and sensor4:
		if sensorCase != 1: #only enter the image open function if status is different than previous status
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "all" + ".png")
			sensorCase = 1
	elif sensor1 and sensor2 and sensor3 and not sensor4:
		if sensorCase != 2:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "123" + ".png")
			sensorCase = 2
	elif sensor1 and sensor2 and sensor4 and not sensor3:
		if sensorCase != 3:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "124" + ".png")
			sensorCase = 3
	elif sensor1 and sensor3 and sensor4 and not sensor2:
		if sensorCase != 4:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "134" + ".png")
			sensorCase = 4
	elif sensor2 and sensor3 and sensor4 and not sensor1:
		if sensorCase != 5:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "234" + ".png")
			sensorCase = 5
	elif sensor1 and sensor2 and not sensor3 and not sensor3:
		if sensorCase != 6:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "12" + ".png")
			sensorCase = 6
	elif sensor1 and sensor3 and not sensor2 and not sensor4:
		if sensorCase != 7:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "13" + ".png")
			sensorCase = 7
	elif sensor1 and sensor4 and not sensor2 and not sensor3:
		if sensorCase != 8:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "14" + ".png")
			sensorCase = 8
	elif sensor2 and sensor3 and not sensor1 and not sensor4:
		if sensorCase != 9:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "23" + ".png")
			sensorCase = 9
	elif sensor2 and sensor4 and not sensor1 and not sensor3:
		if sensorCase != 10:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "24" + ".png")
			sensorCase = 10
	elif sensor3 and sensor4 and not sensor1 and not sensor2:
		if sensorCase != 11:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "34" + ".png")
			sensorCase = 11
	elif sensor1 and not sensor2 and not sensor3 and not sensor4:
		if sensorCase != 12:
			os.system("sudo pkill fbi")
			print ("opening pic 1:")
			#time.sleep(1)
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "1" + ".png")
			sensorCase = 12
	elif sensor2 and not sensor1 and not sensor3 and not sensor4:
		if sensorCase != 13:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "2" + ".png")
			sensorCase = 13
	elif sensor3 and not sensor1 and not sensor2 and not sensor4:
		if sensorCase != 14:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "3" + ".png")
			sensorCase = 14
	elif sensor3 and not sensor1 and not sensor2 and not sensor3:
		if sensorCase != 15:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "testpic" + "4" + ".png")
			sensorCase = 15
	elif not sensor1 and not sensor2 and not sensor3 and not sensor4:
		if sensorCase != 16:
			os.system("sudo pkill fbi")
			os.system("sudo pkill fbi")
			sensorCase = 16
	else:
		if sensorCase != 17:
			os.system("sudo pkill fbi")
			os.system("sudo fbi -a -T 2" + picPath + "snowman.jpg")
			sensorCase = 17

	#time.sleep(.3)

	picPath = " /home/pi/Pictures/"
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	ser.flush()
	ser.write('1')
	time.sleep(.2)



	# if(ser.in_waiting >0):
	#print("writing serial")
	#time.sleep(1)

	if (ser.in_waiting <=0):
		print(ser.in_waiting)


	print("waiting")
	print(ser.in_waiting)
	#time.sleep(1)
	if (ser.in_waiting > 0):
		line = str(ser.readline().strip())
		sensor1 = line[0] == 'T'
		sensor2 = line[1] == 'T'
		sensor3 = line[2] == 'T'
		sensor4 = line[3] == 'T'
		print("serial written")
		if not sensor1 and not sensor2 and not sensor3 and not sensor4:
			print("close the damn picture")
			time.sleep(1)
			os.system("sudo pkill fbi")
		if sensor1 or sensor2 or sensor3 or sensor4:
			os.system("sudo pkill fbi")
			(sensor1, sensor2, sensor3, sensor4) = touchPic(sensor1, sensor2, sensor3, sensor4, sensorCase,
																			picPath)

		#time.sleep(2)
		sensorCase = 0
		#sensor1 = False
		#sensor2 = False
		#sensor3 = False
		#sensor4 = False
	return sensor1, sensor2, sensor3, sensor4

def penalty():
	class ExampleApp(tk.Tk):
		def __init__(self):
			tk.Tk.__init__(self)
			self.label = tk.Label(self, font=('times', 100, 'bold'), bg='white', fg='red',
								  text="Think About Your Choices", width=100, height=50)

			self.label.pack()
			self.remaining = 0
			self.countdown(30)

		def countdown(self, remaining=None):
			if remaining is not None:
				self.remaining = remaining

			if self.remaining <= 0:
				self.label.configure(text="Penalty over. Try not to screw up again.")
				time.sleep(1.5)
				self.destroy()

			else:
				self.label.configure(text="%d" % self.remaining)
				self.remaining = self.remaining - 1
				self.after(1000, self.countdown)

	if __name__ == "__main__":
		app = ExampleApp()
		app.mainloop()