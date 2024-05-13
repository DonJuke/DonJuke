from machine import ADC
from machine import Pin
from time import sleep
from stepper import Stepper
VRx = ADC(25)        # create an ADC object acting on a pin
VRy = ADC(26)        # create an ADC object acting on a pin
SW = ADC(27)        # create an ADC object acting on a pin
VRx.atten(ADC.ATTN_11DB)
VRy.atten(ADC.ATTN_11DB)



enable1 = Pin(19, Pin.OUT)
enable2 = Pin(23, Pin.OUT)
enable3 = Pin(4, Pin.OUT)
stepsperrev=1028
motor1 = Stepper(5,18,steps_per_rev=stepsperrev,speed_sps=200)
motor2 = Stepper(21,22,steps_per_rev=stepsperrev,speed_sps=200)
motor3 = Stepper(15,2,steps_per_rev=stepsperrev,speed_sps=200)

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def changespeed():
        speed = (abs(x-81)*11.5) + 1
        if speed > 900:
            speed = 900
        if speed <= 12:
            speed = 1;
        motor1.speed(speed)
        motor2.speed(speed)
        motor3.speed(speed)

        print("Stepper speed = ",speed)
        return speed

    
state = 1
while True:
    x = VRx.read()
    x = map_range(x,0,4095,0,180)

    y = VRy.read()
    y = map_range(y,0,4095,0,180)
    
    button = bool(SW.read())
    if button == False:
        sleep(.2)
        state = state + 1
        if state >= 5:
            state = 1
    sleep(0.1)

    

    
    print("VRx =", x)
    print("VRy =", y)
    print("Button state:",not(button))
    
    if state == 1:
        print("State = 1")
        enable1.off()
        changespeed()
        if x >= 84:
            motor1.free_run(1)
        if x <= 80:
            motor1.free_run(-1)
        if x >= 81 and x <= 83:
            motor1.free_run(0)
    if state == 2:
        print("State = 2")
        enable1.on()
        enable2.off()
        changespeed()
        if x >= 84:
            motor2.free_run(1)
        if x <= 80:
            motor2.free_run(-1)
        if x >= 81 and x <= 83:
            motor2.free_run(0)
    if state == 3:
        print("State = 3")
        enable2.on()
        enable3.off()
        changespeed()
        if x >= 84:
            motor3.free_run(1)
        if x <= 80:
            motor3.free_run(-1)
        if x >= 81 and x <= 83:
            motor3.free_run(0)
    if state == 4:
        print("State = Off")
        enable1.on()
        enable2.on()
        enable3.on()      



        
    
    

