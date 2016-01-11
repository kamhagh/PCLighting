import math
import time
from Lighting import Controller, Color

class Effects:

	def __init__(self, controller, numLeds = 5):
		self.numLeds = numLeds
		self.Strip = controller

	def rainbow(self, speed = 100):
		pass
	def fade(self, color, speed = 2000):
		now = self.millis()
		if(color.B > 0):
			halfBlue = color.B/2
			blue = halfBlue + halfBlue*math.cos(2*math.pi/speed*now)
		else:
			blue = 0

		if(color.G > 0):
			halfGreen = color.B/2
			green = halfGreen + halfGreen*math.cos(2*math.pi/speed*now)
		else:
			green = 0

		if(color.R > 0):
			halfRed = color.B/2
			red = halfRed + halfRed*math.cos(2*math.pi/speed*now)
		else:
			red = 0

		self.Strip.setAll(Color(int(round(red)), int(round(green)), int(round(blue))))

	def millis(self):
		return int(round(time.time() * 1000))