import serial
import time
import threading
import sys
import os
import random
import math
from Lighting import Controller, Color
from Effects import Effects

def isRunning(process_name):
	# foregroundWindow = GetWindowText(GetForegroundWindow())
	# return process_name in foregroundWindow
	"""not supported in Linux"""
	tmp = os.popen("ps -Af").read()
	return process_name in tmp[:]
	"""Will look for a solution soon, not much needed as i don't game in linux!"""

Strip = Controller()
effect = Effects(Strip, 6)

rainbowTimer = effect.millis()
count = 0

while(True): #should make these automated with a file and save them everytime and maybe make a GUI
	if(effect.millis() - rainbowTimer >= 100): # Should move to a thread or something
		Strip.rainbow(count)
		count += 1
		if(count == 6):
			count = 0
		rainbowTimer = effect.millis()

	if(isRunning("vlc")):
		Strip.setPixel(5, Color(255, 50, 0))
	elif(isRunning("firefox") or isRunning("chrome")):
		Strip.setPixel(5, Color(0, 50, 255))
	else:
		Strip.setPixel(5, Color())
	Strip.sendBuffer()
	time.sleep(0.01)