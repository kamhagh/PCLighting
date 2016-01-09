import serial.tools.list_ports
import serial

class Controller:



	def __init__(self, SerialNumber = "SNR=75331333939351706072", LEDCount = 6):
		self.SerialNumber = SerialNumber
		self.ser = serial.Serial("COM4", 115200)

		self.LEDCount = LEDCount
		self.Buffer = []
		for i in range(0, LEDCount):
			self.Buffer.append(Color())

	def search(self):
		ports = list(serial.tools.list_ports.comports()) #Get all PORTS's info

		for p in ports: #check them all
			if self.SerialNumber in p[2]: #if the serial number matches
				self.ser = serial.Serial(p[0], 115200) # P[0] is port name

	def rainbow(self, startPosition):
		rainbowScale = 192 / self.LEDCount

		for i in range(0, self.LEDCount):
			self.Buffer[i] = self.rainbowOrder((rainbowScale * (i + startPosition)) % 192)

	def setPixel(self, i, color):
		self.Buffer[i] = color

	def sendPixel(self, i, color):
		LEDNumber = i << 24
		redvalue = color.R << 16
		greenvalue = color.G << 8
		bluevalue = color.B
		self.ser.write(str(LEDNumber | redvalue | greenvalue | bluevalue) + '\n')

	def sendBuffer(self):
		for i in range (0, self.LEDCount):
			self.sendPixel(i, self.Buffer[i])

	def setAll(self, color):
		self.checkColor(color)
		for i in range(0, self.LEDCount):
			self.Buffer[i] = color

	def clearAll(self):
		self.ser.write("251658240\n"); # Sending char 'C' clears all

	def checkColor(self, color):
		if(color.R > 255 or color.G > 255 or color.B > 255):
			raise "Color must be less then 255"

		if(color.R < 0 or color.G < 0 or color.B < 0):
			raise "Color must be bigger then 0"

	def rainbowOrder(self, position):
		result = Color()

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



class Color:

	def __init__(self, Red = 0, Green = 0, Blue = 0):
		self.R = Red
		self.B = Blue
		self.G = Green

	def set(self, Red = 0, Green = 0, Blue = 0):
		self.R = Red
		self.B = Blue
		self.G = Green