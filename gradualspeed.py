import pygame
import time
import RPi.GPIO as GPIO
import disdik

# -----------------Define Variables---------------------


# Pins to be used stored in list
PIN_RB = 17
PIN_RF = 18
PIN_LB = 22
PIN_LF = 23
pins = [PIN_RB,PIN_RF,PIN_LB,PIN_LF]

#Loop until the user clicks the options button.
done = False

# Some very useful info about DUALSHOCK 4 Controller (Pre-processed through ds4drv):
buttonNames = {0: 'Square',1: 'X',2: 'Circle',3: 'Triangle',4: 'L1',5: 'R1',6: 'L2',7: 'R2',8: 'Share',9: 'Options',10: 'L3',11: 'R3',12: 'PS',13: 'TouchPad'}
axisNames = {0:'Leftanalog X',1:'LeftAnalog Yinverted',2:'RightAnalog X',3:'L2',4:'R2',5:'RightAnalog Yinverted',6:'Roll',7:'Pitch',8:'clown',9:'garbage',10:'garbage',11:'garbage',12:'garbage'}

# -----------------Set up/Initialize Core Objects---------------------

# Set up GPIO for output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)

# global frequency for all PWM pins
freq = 50

#set up pins
pin_rf = GPIO.PWM(PIN_RF, freq)
pin_rb = GPIO.PWM(PIN_RB, freq)
pin_lf = GPIO.PWM(PIN_LF, freq)
pin_lb = GPIO.PWM(PIN_LB, freq)

pin_rf.start(0)
pin_rb.start(0)
pin_lf.start(0)
pin_lb.start(0)

#------Pygame setup------#
pygame.init()

# Initialize the joysticks
pygame.joystick.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -----------------Define Functions---------------------

def goForward(speed):
	pin_rb.ChangeDutyCycle(0)
	pin_lb.ChangeDutyCycle(0)
	pin_rf.ChangeDutyCycle(speed)
	pin_lf.ChangeDutyCycle(speed)


def goBackward():
	pin_rf.ChangeDutyCycle(0)
	pin_lf.ChangeDutyCycle(0)
	pin_rb.ChangeDutyCycle(speed)
	pin_lb.ChangeDutyCycle(speed)

def halt():
	pin_rf.ChangeDutyCycle(0)
	pin_rb.ChangeDutyCycle(0)
	pin_lf.ChangeDutyCycle(0)
	pin_lb.ChangeDutyCycle(0)

def processInputs(xValue, yValue):
    if(yValue > 0):
        goForward(yValue)
    else:
    	goBackward(-yValue)



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
