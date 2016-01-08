#include "Adafruit_NeoPixel.h"
#include "WS2812_Definitions.h"

#define PIN 4
#define LED_COUNT 5

struct pixel {
  int R = 0;
  int B = 0;
  int G = 0;
};

Adafruit_NeoPixel leds = Adafruit_NeoPixel(LED_COUNT, PIN, NEO_GRB + NEO_KHZ800);

bool runState = true;
long lastRecieve = 0; 
int pixelNumber = 0;
struct pixel tempPixel;
//struct pixel Pixels[LED_COUNT];

void setup()
{
  Serial.begin(115200);
  leds.begin();  // Call this to start up the LED strip.
  clearLEDs();   // This function, defined below, turns all LEDs off...
  leds.show();   // ...but the LEDs don't actually update until you call this.
}

void loop() {
  if(Serial.available() > 0) {
    runState = true;
    lastRecieve = millis();
    /*
    you will need to write your own way of receiving input and determining when to loop in here...
     I am just including the part that sets the color picked above.
     pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
     */

    long hexval= PC_Receive(); // You sent: 0x01FF8C3C or, integer value,33524796
    if(hexval == 251658240) {
      clearLEDs();
      leds.show();
    }
    int led=hexval >> 24;
    int r = hexval >> 16 & 0xFF;
    int g = hexval >> 8 & 0xFF;
    int b = hexval & 0xFF;
    leds.setPixelColor(led,r,g,b); //LED 1 as color FF8C3C
    leds.show();
    //    delay(500);
  } else if((millis() - lastRecieve) >= 2000) {
    if(runState) {
      clearLEDs();
      leds.show();
    }
    runState = false;
    delay(50);
  }
}

void setPixelColor(int a, struct pixel P)
{
  leds.setPixelColor(a, P.R, P.G, P.B);
}

long PC_Receive() {
  String inString = "";
  int inChar = 0;
  do {
    while(Serial.available() == 0);
    inChar = Serial.read();
    if(isDigit(inChar)) {
      inString += (char)inChar;
    }

  } 
  while(inChar != '\n');

  return inString.toInt();
}







void setColourRgb(unsigned int red, unsigned int green, unsigned int blue) {
  for(int i = 0; i < LED_COUNT; i++) {
    leds.setPixelColor(i, red, green, blue);
  }
  leds.show();
}


void clearLEDs()
{
  for (int i=0; i<LED_COUNT; i++)
  {
    leds.setPixelColor(i, 0);
  }
}

void rainbow(byte startPosition) 
{
  // Need to scale our rainbow. We want a variety of colors, even if there
  // are just 10 or so pixels.
  int rainbowScale = 192 / LED_COUNT;

  // Next we setup each pixel with the right color
  for (int i=0; i<LED_COUNT; i++)
  {
    // There are 192 total colors we can get out of the rainbowOrder function.
    // It'll return a color between red->orange->green->...->violet for 0-191.
    leds.setPixelColor(i, rainbowOrder((rainbowScale * (i + startPosition)) % 192));
  }
  // Finally, actually turn the LEDs on:
  leds.show();
}

// Input a value 0 to 191 to get a color value.
// The colors are a transition red->yellow->green->aqua->blue->fuchsia->red...
//  Adapted from Wheel function in the Adafruit_NeoPixel library example sketch
uint32_t rainbowOrder(byte position) 
{
  // 6 total zones of color change:
  if (position < 31)  // Red -> Yellow (Red = FF, blue = 0, green goes 00-FF)
  {
    return leds.Color(0xFF, position * 8, 0);
  }
  else if (position < 63)  // Yellow -> Green (Green = FF, blue = 0, red goes FF->00)
  {
    position -= 31;
    return leds.Color(0xFF - position * 8, 0xFF, 0);
  }
  else if (position < 95)  // Green->Aqua (Green = FF, red = 0, blue goes 00->FF)
  {
    position -= 63;
    return leds.Color(0, 0xFF, position * 8);
  }
  else if (position < 127)  // Aqua->Blue (Blue = FF, red = 0, green goes FF->00)
  {
    position -= 95;
    return leds.Color(0, 0xFF - position * 8, 0xFF);
  }
  else if (position < 159)  // Blue->Fuchsia (Blue = FF, green = 0, red goes 00->FF)
  {
    position -= 127;
    return leds.Color(position * 8, 0, 0xFF);
  }
  else  //160 <position< 191   Fuchsia->Red (Red = FF, green = 0, blue goes FF->00)
  {
    position -= 159;
    return leds.Color(0xFF, 0x00, 0xFF - position * 8);
  }
}

