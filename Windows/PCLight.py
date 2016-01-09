import serial
import time
import threading
import random
import math
from win32gui import GetWindowText, GetForegroundWindow
from Lighting import Controller, Color
from Effects import Effects

def isRunning(process_name):
	foregroundWindow = GetWindowText(GetForegroundWindow())
	return process_name in foregroundWindow

Strip = Controller()
effect = Effects(Strip, 5)

rainbowTimer = effect.millis()
count = 0

while(True): #should make these automated with a file and save them everytime and maybe make a GUI
	if(isRunning("VLC")):
		Strip.setAll(Color(255, 50, 0))
	elif(isRunning("Mozilla Firefox")):
		Strip.setAll(Color(0, 50, 255))
	elif(isRunning("Heroes of the Storm")): # Add fading and stuff?
		effect.fade(Color(50, 0, 255), 4000)
	else:
		if(effect.millis() - rainbowTimer >= 100): # Should move to a thread or something
			Strip.rainbow(count)
			count += 1
			if(count == 5):
				count = 0
			rainbowTimer = effect.millis()
	time.sleep(0.01)
	Strip.sendBuffer()