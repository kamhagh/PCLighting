import serial
import time
import threading
import random
import math
from win32gui import GetWindowText, GetForegroundWindow
from Lighting import Controller, Color
from Effects import Effects
from ConfigParser import SafeConfigParser

def isRunning(process_name):
	foregroundWindow = GetWindowText(GetForegroundWindow())
	return process_name in foregroundWindow

def LoadProfiles():
	lines = open("profile.txt").readlines()
	for i in lines:
		tmplist = []
		tmp = i.split(":")
		tmpColor = tmp[2].split(',')
		toSetColor = Color(int(tmpColor[0]), int(tmpColor[1]), int(tmpColor[2]))
		tmplist = [tmp[0], tmp[1], toSetColor]
		Profiles.append(tmplist)

Profiles = []

LoadProfiles()

Strip = Controller()
effect = Effects(Strip)

rainbowTimer = effect.millis()
count = 0

Strip.setAll(Color(255,0,255))
Strip.sendBuffer()

while(True): #should make these automated with a file and save them everytime and maybe make a GUI
	if(effect.millis() - rainbowTimer >= 100): # Should move to a thread or something
		Strip.rainbow(count)
		count += 1
		if(count == 6):
			count = 0
		rainbowTimer = effect.millis()

	# Strip.setPixel(5, Color(255, 255, 255))
	effect.fade(Color(255,255,255), 5000)

	for i in Profiles:
		if(isRunning(i[0])):
			if(i[1] == 'F'):
				effect.fade(i[2], 5000)
			else:
				Strip.setPixel(5, i[2])


	# if(isRunning("VLC")):
	# 	Strip.setPixel(5, Color(255, 50, 0))
	# elif(isRunning("Mozilla Firefox")):
	# 	Strip.setPixel(5, Color(0, 50, 255))
	# elif(isRunning("Heroes of the Storm")): # Add fading and stuff?
	# 	effect.fade(Color(50, 0, 255), 4000)
	# else:
	# 	Strip.setPixel(5, Color())
	Strip.sendBuffer()
	time.sleep(0.01)