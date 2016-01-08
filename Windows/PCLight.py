import serial
import time
import threading
import random
from win32gui import GetWindowText, GetForegroundWindow
from Lighting import Controller, Color

def isRunning(process_name):
	foregroundWindow = GetWindowText(GetForegroundWindow())
	return process_name in foregroundWindow

def millis():
	return int(round(time.time() * 1000))

Strip = Controller()

count = 0
rainbowTimer = millis()

while(True): #should make these automated with a file and save them everytime and maybe make a GUI
	if(isRunning("VLC")):
		Strip.setAll(Color(255, 50, 0))
	elif(isRunning("Mozilla Firefox")):
		Strip.setAll(Color(0, 50, 255))
	elif(isRunning("Heroes of the Storm")): # Add fading and stuff?
		Strip.setAll(Color(50, 0, 255))
	else:
		if(millis() - rainbowTimer >= 100): # Should move to a thread or something
			Strip.rainbow(count)
			count += 1
			if(count == 5):
				count = 0
			rainbowTimer = millis()
	Strip.sendBuffer()