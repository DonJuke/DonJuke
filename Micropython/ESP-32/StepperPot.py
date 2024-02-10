from machine import ADC
from time import sleep
from stepper import Stepper
import math

pot = ADC(15)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_9BIT)
pot_values = []
std = 0
stepsperrev=200
speed=200

stepper = Stepper(18,19,steps_per_rev=stepsperrev,speed_sps=speed)
stepper.overwrite_pos(0)
position = 0
setpoint = 0


def getSetpoint():
    global setpoint
    global pot_values
    global position
    for i in range(-1,20):
      pot_values.append(int(round(pot.read_uv()-128000)/3000000*stepsperrev))
      mean = sum(pot_values) / len(pot_values)  # mean
      var  = sum(pow(x-mean,2) for x in pot_values) / len(pot_values)  # variance
      std  = math.sqrt(var)  # standard deviation
      maximum = max(pot_values)
      minimum = min(pot_values)

    setpoint = round(mean)
    position = stepper.get_pos()
    position_deg = int (position/stepsperrev*360)
    setpoint_deg = int(setpoint/stepsperrev*360)
    #stepper.overwrite_pos(setpoint)
    print ('Standard Deviation:', std,'Setpoint:',setpoint_deg,'Position:',position_deg)
    #print ('Mean:',mean)
    #print('Maximum:',maximum)
    #print('Minimum:',minimum)
    pot_values = []

    
    
def giveStepperCommands():
    global setpoint
    global pot_values
    global position

    while setpoint != position:
        getSetpoint()
        position = stepper.get_pos()
        pot_values = []
        stepper.track_target()
        stepper.target(setpoint)
        sleep(0.03)
        stepper.stop()
        break
        

                
        #print(pot_values)
    print ('Standard Deviation:', std,'Setpoint:',setpoint,'Position:',position)
    pot_values = []
        
    

    
while True:
    getSetpoint()
    giveStepperCommands()
    
    
    
    

        
  

  