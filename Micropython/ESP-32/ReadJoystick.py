from machine import ADC
from time import sleep
VRx = ADC(25)        # create an ADC object acting on a pin
VRy = ADC(26)        # create an ADC object acting on a pin
SW = ADC(27)        # create an ADC object acting on a pin


def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    x = VRx.read()
    x = map_range(x,0,4095,0,180)

    y = VRy.read()
    y = map_range(y,0,4095,0,180)
    
    button = bool(SW.read())
    
    print(x)
    print(y)
    print(button)
    
    sleep(.1)
    
    

