"""TurtlebotCon controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import csv
from math import sqrt,atan2,pi,fabs
from numpy import arctan
 



# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


TIME_STEP = 16
MAX_SPEED = 8
HALF_SPEED = 4
BASE_SPEED = 1
SAFETY_DISTANCE = 0.40

# Robot instance
#robot = Robot()

# Get components of robot
lidar = robot.getDevice('Hokuyo URG-04LX-UG01')

# Enable motors
leftMotor = robot.getDevice('wheel_left_joint')
rightMotor = robot.getDevice('wheel_right_joint')

#Enable GPs
gps = robot.getDevice('gps')
gps.enable(timestep)

#Enable Compass
compass = robot.getDevice('compass')
compass.enable(timestep)

#Enable lidar
lidar.enable(TIME_STEP)
lidar.enablePointCloud() 

#Variables
lidarWidth = lidar.getHorizontalResolution()
lidarMaxRange = lidar.getMaxRange()
loopCounter = 0

#  FUNCTIONS 
def moveForward():
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(MAX_SPEED)
    rightMotor.setVelocity(MAX_SPEED)
    #print("Moving forward")
    return(MAX_SPEED, MAX_SPEED)

def turnLeft():    
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(HALF_SPEED/9)
    rightMotor.setVelocity(HALF_SPEED)
    #print("Turning left")
    return(HALF_SPEED/9, HALF_SPEED)
    
def turnRight():    
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(HALF_SPEED)
    rightMotor.setVelocity(HALF_SPEED/9)
    #print("Turning right")
    return(HALF_SPEED, HALF_SPEED/9)
    
def rotateLeft():
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(-BASE_SPEED)
    rightMotor.setVelocity(BASE_SPEED)
    #print("Rotating left")
    return(-BASE_SPEED, BASE_SPEED)
    
def rotateRight():
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(BASE_SPEED)
    rightMotor.setVelocity(-BASE_SPEED)
    #print("Rotating right")
    return(BASE_SPEED, -BASE_SPEED)
    
    
def moveBackward():
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(-BASE_SPEED)
    rightMotor.setVelocity(-BASE_SPEED)
    #print("Moving backward")
    return(-BASE_SPEED, -BASE_SPEED)

def stop():
    leftMotor.setPosition(0) # Set position es absoluto o relativo?
    rightMotor.setPosition(0)
    leftMotor.setVelocity(0)
    rightMotor.setVelocity(0)
    #print("Stopping")
    return (0, 0)
    
def obstacle_evasion(room,x1,y1):
    #Detection of obstacle infront using lidar
    rangeVec = lidar.getRangeImage()
    #print("in obstacle evasion")
    front_left = (rangeVec[332]) < 1
    front_right = (rangeVec[443]) < 1
    mid_left = (rangeVec[221]) < 1
    mid_right = (rangeVec[554]) < 1
    back_left = (rangeVec[110]) < 0.5
    back_right = (rangeVec[666]) < 0.5              
    # lidar values divide into sections
    """
    print("front_left: ", front_left)
    print("front_right: ", front_right)
    print("mid_left: ", mid_left)
    print("mid_right: ", mid_right)
    """
    # Reactive action according to obstacle infront
    if front_left and front_right:
        rotateLeft()
        return 1
    elif front_right or mid_right or back_right:
           turnLeft() 
           return 1
    elif front_left or mid_left or back_left:
           turnRight()
           return 1
    else: 
        return goal(room,x1,y1)
        

def angleCalc(x1,y1):
    #print("angle calc")
    
    cord = gps.getValues()
    x = round(cord[0],2)
    y = round(cord[1],2)
    #print("Coordinates:",x,y)
    requiredO = atan2(  x1- x , y1- y)* 180.0/pi#theta need to be achieved
    
    
    north = compass.getValues() 
    O = atan2(north[1], north[0])* 180.0/pi# Theta of bot
    
        
    #print("requiredO:",requiredO)
    #print("O:",O)
    
    angle =  ( requiredO - O)
    
    
    print("angle:",angle)
    
    if angle <= -25 : 
        rotateLeft()
    elif angle >= 25 : 
        rotateRight()
    else:
        moveForward()

def goal(pos,x1,y1):
    #print("in goal")
    if pos != room_in() :
        stop()
        return 0
    else:
        angleCalc(x1,y1)
        return 1
        
#room positions in this scenario        
def room_in():
    x,y,z = gps.getValues()
    if (-5.2 <= x <= 4) and (-4 <= y <= 8):
        return 1 #hall
    elif (4 <= x <= 10) and (4 <= y <= 9):
        return 2 #coridor
    elif (-5.2 <= x <= 6) and (8 <= y <= 16):
        return 3 #library
    elif (4 <= x <= 16) and (-4 <= y <= 8):
        return 4 #studio
    elif (12 <= x <= 16) and (8 <= y <= 16):
        return 5 #bedroom
    elif (-12 <= x <= -5.2) and (-4 <= y <= 10): 
        return 6 #living room
    elif (-16 <= x <= -12) and (-4 <= y <= 16):  
        return 7 #vernada
    elif (-12 <= x <= -5.2) and (10 <= y <= 16):
        return 8 #kitchen
    elif (6 <= x <= 12) and (8 <= y <= 16):
        return 9 #bathroom
    else:
        return 0
#defined north south east west for every room  for calculation of route
def nsew(room):
    if room == 1:
        return ((-2.6,12),(None,None),(4.5,7),(-8,-2))
    if room == 2:
        return ((9,12),(10,2),(14,12),(3,5))
    if room == 3:
        return ((None,None),(-2.5,6),(None,None),(None,None))
    if room == 4:
        return ((12,6),(None,None),(None,None),(None,None))
    if room == 5:
        return ((None,None),(None,None),(None,None),(12,6))
    if room == 6:
        return ((-8,12),(None,None),(-1,0),(-14,6))
    if room == 7:
        return ((None,None),(None,None),(-11,6),(None,None))
    if room == 8:
        return ((None,None),(-6,6),(None,None),(None,None))
    if room == 9:
        return ((None,None),(8,5.5),(None,None),(None,None))
    if room == 0:
        return 0
flag = 0
room = 0
x1,y1=(0,0)

#getting the ouput as input
f = open('annabell_output.txt')
input = list(f)
ind = 0
#print(input)

# Main loop:

while robot.step(timestep) != -1:
    #x,y,z = gps.getValues()
    #print("current cord:",x,y)
    try:   
        
        #Fetching coordinates for dedicated room
        if  flag == 0:
            flag = 1
            
            room = room_in()
            #print("Room:",room)
            
            getd = input[ind][:-1]
            
            dcoords = nsew(room)
            if getd == 'north':
                x1,y1=dcoords[0]
            elif getd == 'south':
                x1,y1=dcoords[1]
            elif getd == 'east':
                x1,y1=dcoords[2]
            elif getd == 'west':
                x1,y1=dcoords[3] 
            else:
                flag = 0 
            ind = ind + 1
            print("input:",getd)
            #print("index:", ind)          
        else:
            if x1 == None and y1 == None:
                flag = 0
            else:
                flag = obstacle_evasion(room,x1,y1)
        #print("goto cord:" , x1 , y1 )
        #
        #print("Loop count: ", loopCounter)
        loopCounter = loopCounter + 1
    except:
        print("End of simulation")
        break
        
    
    # Enter here exit cleanup code.
    
