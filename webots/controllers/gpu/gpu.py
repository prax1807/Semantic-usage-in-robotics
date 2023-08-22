"""gpu controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

BASE_SPEED = 10
X = 3.00
Y = 3.00
def moveForward(leftMotor,rightMotor):
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(BASE_SPEED)
    rightMotor.setVelocity(BASE_SPEED)
    print("Moving forward")
    return(0)

def stop(leftMotor,rightMoto):
    leftMotor.setPosition(0) # Set position es absoluto o relativo?
    rightMotor.setPosition(0)
    leftMotor.setVelocity(0)
    rightMotor.setVelocity(0)
    print("Stopping")
    return (0, 0)
     
def moveBackward(leftMotor,rightMotor):
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    leftMotor.setVelocity(-BASE_SPEED)
    rightMotor.setVelocity(-BASE_SPEED)
    print("Moving backward")
    return(0)
        
def run_robot(robot):
    timestep = 64
    max_speed = 6.28
    
    leftMotor = robot.getDevice('wheel_left_joint')
    rightMotor = robot.getDevice('wheel_right_joint')
    
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    
    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)
    
    gps = robot.getDevice('gps')
    gps.enable(timestep)
    # Main loop:
    
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
        #print(timestep)
        c = 0
        gps_val = gps.getValues()
        while (gps_val[0]!= X):
            if gps_val[0] < X:
                moveForward(leftMotor,rightMotor)
            elif gps_val[1] > X:
                moveBackward(leftMotor,rightMotor)
        
        stop(leftMotor,rightMotor)
              
        
        while (gps_val[1]!=Y):
            if gps_val[1] < Y:
                moveForward(leftMotor,rightMotor)
            elif gps_val[1] > X:
                moveBackward(leftMotor,rightMotor) 
        
            
        # Process sensor data here.
        gps_new_val = gps.getValues()
        print (gps_val)
        print(timestep)
        for i in range(3):
            change[i] = gps_val[i] - gps_new_val[i]
        print(change)
        
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        
        c += moveForward(leftMotor,rightMotor)
        print(c)
        
        pass
    
    # Enter here exit cleanup code.
    
# create the Robot instance.
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
    

