import pygame
import time
import RPi.GPIO as GPIO

# -----------------Define Variables---------------------

# All GPIO pins that will be used
pins = [17, 18, 22, 23]

# Convenient naming of GPIO pin numbers
PIN_RB = 17
PIN_RF = 18
PIN_LB = 22
PIN_LF = 23

robotState = "Idle"

#Loop until the user clicks the options button.
done = False

# Some very useful info about DUALSHOCK 4 Controller (Pre-processed through ds4drv):
buttonNames = {0: 'Square',1: 'X',2: 'Circle',3: 'Triangle',4: 'L1',5: 'R1',6: 'L2',7: 'R2',8: 'Share',9: 'Options',10: 'L3',11: 'R3',12: 'PS',13: 'TouchPad'}
axisNames = {0:'Leftanalog X',1:'LeftAnalog Yinverted',2:'RightAnalog X',3:'L2',4:'R2',5:'RightAnalog Yinverted',6:'Roll',7:'Pitch',8:'clown',9:'garbage',10:'garbage',11:'garbage',12:'garbage'}

# -----------------Set up/Initialize Core Objects---------------------

# Set up GPIO for output
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
    
pygame.init()

# Initialize the joysticks
pygame.joystick.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -----------------Define Functions---------------------

def goForward():
    GPIO.output(PIN_RF, 1)
    GPIO.output(PIN_LF, 1)

def goBackward():
    GPIO.output(PIN_RB, 1)
    GPIO.output(PIN_LB, 1)

def halt():
    GPIO.output(PIN_RF, 0)
    GPIO.output(PIN_LF, 0)
    GPIO.output(PIN_RB, 0)
    GPIO.output(PIN_LB, 0)

def processInputs(xValue, yValue):
    global robotState
    if(yValue > 0.5):
        if(robotState != "Forward"):
            print("Going Forward")
            goForward()
            robotState = "Forward"
    elif(yValue < -0.5):
        if(robotState != "Backward"):
            print("Going Backward")
            goBackward()
            robotState = "Backward"
    else:
        if(robotState != "Idle"):
            print("Stopping")
            halt()
            robotState = "Idle"

# -----------------Begin Program---------------------

print("Program starting. Press options to quit")

while done==False:

    # Handle any events that may have occured
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if(event.__dict__["button"] == 9):
                done = True

    # Get default system Joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # X,Y values of right analog stick
    yValue = -joystick.get_axis(5)
    xValue = joystick.get_axis(2)

    processInputs(xValue,yValue)

    # Poll controller at 20 FPS
    clock.tick(20)
    
# -----------------End Program---------------------

print("Program Closing. D-D-D-D-D-D-D-D-D-DEUCEZ")
pygame.quit()
