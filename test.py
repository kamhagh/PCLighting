import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "SNR=75331333939351706072" in p[2]:
    	print "ARDUINO! "