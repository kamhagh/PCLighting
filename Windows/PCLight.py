import serial
import time
from win32gui import GetWindowText, GetForegroundWindow
from Lighting import Controller, Color
from Effects import Effects

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

while(True):
	if(effect.millis() - rainbowTimer >= 100): # Should move to a thread or something
		Strip.rainbow(count)
		count += 1
		if(count == 6):
			count = 0
		rainbowTimer = effect.millis()

	effect.fade(Color(255,255,255), 5000)

	for i in Profiles:
		if(isRunning(i[0])):
			if(i[1] == 'F'):
				effect.fade(i[2], 5000)
			else:
				Strip.setPixel(5, i[2])

	Strip.sendBuffer()
	time.sleep(0.01)