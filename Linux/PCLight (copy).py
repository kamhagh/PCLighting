import serial
import time
import random
import os
import sys



class Pixel:
	R = 0
	G = 0
	B = 0

	def set(self, R, G, B):
		self.R = R
		self.G = G
		self.B = B

def isRunning(process_name):
	tmp = os.popen("ps -Af").read()
	return process_name in tmp[:]

def clearAll():
		ser.write("251658240\n"); # Sending char "C clears all"

def sendPixel(pixels):
	for i in range(0,5):
		#print "Pixel(" + str(i) + ") : " + str(pixels[i].R) + " " + str(pixels[i].G) + " " + str(pixels[i].B)
		LEDNumber = i << 24
		redvalue = pixels[i].R << 16
		greenvalue = pixels[i].G << 8
		bluevalue = pixels[i].B
		ser.write(str(LEDNumber | redvalue | greenvalue | bluevalue) + '\n')

def rainbowOrder(position):
	result = Pixel()

	if position < 31:
		result.set(0xFF, position * 8, 0)

	elif position < 63:
		position -= 31
		result.set(0xFF - position * 8, 0xFF, 0)

	elif position < 95:
		position -= 63
		result.set(0, 0xFF, position * 8);

	elif position < 127:
		position -= 95
		result.set(0, 0xFF - position * 8, 0xFF)

	elif position < 159:
		position -= 127
		result.set(position * 8, 0, 0xFF);

	else:
		position -= 159
		result.set(0xFF, 0x00, 0xFF - position * 8)

	return result


def rainbow(startPosition):
	rainbowScale = 192 / 5 #ledcount
	tosend = [0, 0, 0, 0, 0]

	for i in range(0, 5):
		tosend[i] = rainbowOrder((rainbowScale * (i + startPosition)) % 192)
	sendPixel(tosend)

def setAll(pixel):
	tosend = [0,0,0,0,0]
	for i in range(0,5):
		tosend[i] = pixel
	sendPixel(tosend)

# usbplace = raw_input("USB num: ")
ser = serial.Serial('/dev/ttyACM1', 115200)

little = [0,0,0,0,0]
for i in range(0,5):
	little[i] = Pixel()

toset = Pixel()
while(True):
	if(isRunning("vlc")):
		toset.set(255,50,0)
		setAll(toset)
	elif(isRunning("chrome")):
		toset.set(0, 50, 255)
		setAll(toset)
	else:
		for i in range(0, 5):
			rainbow(i)
			time.sleep(0.1)
