Lighting for my PC (top, bottom inside or all!)

Arduino Recieves a number (0xFFFFFFF);
the first 3x2 bits are color
the last bit bit is LED Number with 10bits free for Commands or other stuff
will be moved to bare AVR code as I'm not using Arduino firmware (i might not, there's no point doing this in AVR as i already know how and it's not a commerical product!) and i will use a digiSpark arduino board as it is like a usb flash and is exactly what i need! (with some unused ports :S, maybe i will use normal leds for the other parts)

PC Side is hardcoded and in python for now. I might move it to a thread to eas up things and remove that stupid sendBuffer() and use a new way to  send data

the linux version searchs the usb slots of serial number of my Arduino I'm not sure how to do that on windows, it's more important for now to work on other stuff!