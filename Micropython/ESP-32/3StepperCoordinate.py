from machine import ADC
from time import sleep
from stepper import Stepper
import math
import mtx

stepsperrev=200
speed = 200
xstepper = Stepper(18,19,steps_per_rev=stepsperrev,speed_sps=speed)
ystepper = Stepper(21,0,steps_per_rev=stepsperrev,speed_sps=speed)
zstepper = Stepper(22,23,steps_per_rev=stepsperrev,speed_sps=speed)
xstepper.overwrite_pos_deg(0)
ystepper.overwrite_pos_deg(0)
zstepper.overwrite_pos_deg(0)

link1=10
link2=10
link3=10
theta1=0
theta2=0
theta3=0

def Errorcheck():
    p = (x**2 + y**2 +z**2)**0.5
    if coords[0] >  (link2 + link3):
        print('you cannot fucking do that dumbass')
        raise
    if coords[1] >  (link2 + link3):
        print('you cannot fucking do that dumbass')
        raise
    if coords[2] >  (link1 + link2 + link3):
        print('you cannot fucking do that dumbass')
        raise
    print(coords)
    

try:
    xyz = input("Enter XYZ coordinates bitch (ex: 102 36 74): ")
    coords = [int(tkn) for tkn in xyz.split()] 
    coords.append(1.0)
    x = coords[0]
    y = coords[1]
    z = coords[2]
    print('X:',x)
    print('Y:',y)
    print('Z:',z)
    Errorcheck()
    t1 = [[math.cos(theta1), -math.sin(theta1), 0, 0],
         [math.sin(theta1), math.cos(theta1), 0, 0],
         [0, 0, 1, link1],
         [0, 0, 0, 1]]
    t2 = [[math.cos(theta2), 0, math.sin(theta2), 0],
         [math.sin(theta2), math.cos(theta2), 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1]]
    t3 = [[math.cos(theta3), -math.sin(theta3), 0, link2*math.cos(theta3)],
         [math.sin(theta3), math.cos(theta3), 0, link2*math.sin(theta3)],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    Transform = mtx.mul(t1, coords) 
    Transform1 = mtx.mul(t2, Transform)
    Transform2 = mtx.mul(t3, Transform1)
    print('Coordinates to object:')
    print('Frame 0 to 1', Transform)
    print('Frame 1 to 2', Transform1)
    print('Frame 2 to 3', Transform2)

    xyproj = (y**2 + x**2)**0.5
    yzproj = (y**2 + z**2)**0.5
    xzproj = (x**2 + z**2)**0.5
    theta1 = abs(math.degrees(math.atan(coords[1]/coords[0])))
    theta2 = abs(math.degrees(math.atan(Transform1[1]/Transform1[0])))
    theta3 = abs(math.degrees(math.atan(Transform2[1]/Transform2[0])))

    print('Alpha:',theta1,'Beta:',theta2,'Gamma',theta3)
    print('xyproj:',xyproj,'yzproj:',yzproj,'xzproj:',xzproj)               
except ValueError:      
    print('Invalid integer format: {}'.format(tkn), 'fucking idiot')
    raise

xstep=(theta1/90*200)
ystep=(theta2/90*200)
zstep=(theta3/90*200)
print('xstep:',xstep,'ystep:',ystep,'zstep',zstep)
xstepper.target(theta1)
ystepper.target(theta2)
zstepper.target(theta3)





