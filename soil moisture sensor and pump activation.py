#Micro:Bit Soil Moisture Sensor and Pump Activation
#Created 7-12-18 @ GCDS by Sam, Leon, and Doug

from microbit import *
from time import sleep

while True:
    moisture = pin0.read_analog() #Reads moisture levels from sensor connected to pin #0 and ground
    #display.scroll(moisture,delay=125) # This will scroll the moisture reading on the Micro:bit
    
    if moisture < 50: #Remember to recalibrate this number to your soil wet/dry
        pin1.write_digital(0) #The pump is off
        display.show(Image.HAPPY)
    else:
        pin1.write_digital(1) #The pump is on
        display.show(Image.SAD)
