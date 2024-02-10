from machine import ADC
from stepper import Stepper
import math
from time import sleep

pot1 = ADC(2)
pot2 = ADC(2)
pot3 = ADC(2)
pot1.atten(ADC.ATTN_11DB)
pot2.atten(ADC.ATTN_11DB)
pot3.atten(ADC.ATTN_11DB)
pot1.width(ADC.WIDTH_9BIT)
pot2.width(ADC.WIDTH_9BIT)
pot3.width(ADC.WIDTH_9BIT)

pot1_values = []
pot2_values = []
pot3_values = []
std1 = 0
std2 = 0
std3 = 0
stepsperrev=200
speed = 200
xstepper = Stepper(18,19,steps_per_rev=stepsperrev,speed_sps=speed)
ystepper = Stepper(21,0,steps_per_rev=stepsperrev,speed_sps=speed)
zstepper = Stepper(22,23,steps_per_rev=stepsperrev,speed_sps=speed)
xstepper.overwrite_pos_deg(0)
ystepper.overwrite_pos_deg(0)
zstepper.overwrite_pos_deg(0)

position = 0
while True:
    for i in range(-1, 33):
      pot1_values.append(pot1.read_uv()/3128000*stepsperrev)
      pot2_values.append(pot2.read_uv()/3128000*stepsperrev)
      pot3_values.append(pot3.read_uv()/3128000*stepsperrev)
    mean1 = sum(pot1_values) / len(pot1_values)   # mean
    mean2 = sum(pot1_values) / len(pot1_values)   # mean
    mean3 = sum(pot1_values) / len(pot1_values)   # mean
    var1  = sum(pow(x-mean1,2) for x in pot1_values) / len(pot1_values)  # variance
    var2  = sum(pow(x-mean2,2) for x in pot2_values) / len(pot2_values)  # variance
    var3  = sum(pow(x-mean3,2) for x in pot3_values) / len(pot3_values)  # variance
    std1  = math.sqrt(var1)  # standard deviation
    std2  = math.sqrt(var2)  # standard deviation
    std3  = math.sqrt(var3)  # standard deviation
    

    setpoint1 = round(mean1)
    setpoint2 = round(mean2)
    setpoint3 = round(mean3)
    pot1_values = []
    pot2_values = []
    pot3_values = []
    xposition = xstepper.get_pos()
    yposition = ystepper.get_pos()
    zposition = zstepper.get_pos()
    position1_deg = xposition/stepsperrev*360
    setpoint1_deg = setpoint1/stepsperrev*360
    position2_deg = yposition/stepsperrev*360
    setpoint2_deg = setpoint2/stepsperrev*360
    position3_deg = zposition/stepsperrev*360
    setpoint3_deg = setpoint3/stepsperrev*360
    print ('Motor 1 Standard Deviation:', std1,'Setpoint:',setpoint1_deg,'Position:',position1_deg)
    print ('Motor 2 Standard Deviation:', std2,'Setpoint:',setpoint2_deg,'Position:',position2_deg)
    print ('Motor 3 Standard Deviation:', std3,'Setpoint:',setpoint3_deg,'Position:',position3_deg)
    #print ('Mean:',mean)
    #print('Maximum:',maximum)
    #print('Minimum:',minimum)

    if setpoint1 != xposition:
        round(setpoint1)
        xstepper.target(setpoint1)
        xstepper.track_target()
    if setpoint2 != yposition:
        round(setpoint2)
        ystepper.target(setpoint2)
        ystepper.track_target()
    if setpoint3 != zposition:
        round(setpoint3)
        zstepper.target(setpoint3)
        zstepper.track_target()
        
        
        
        
        
        
        
        
        
    

    sleep(0.1)
    xstepper.stop()
    ystepper.stop()
    zstepper.stop()
