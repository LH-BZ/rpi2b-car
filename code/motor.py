# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

class motor():
    speed = 0
    def __init__(self, pin1, pin2):
        self.pin = [pin1, pin2]
        GPIO.setup(self.pin[0], GPIO.OUT)
        GPIO.setup(self.pin[1], GPIO.OUT)
        self.pwm = [GPIO.PWM(self.pin[0], 100),
                    GPIO.PWM(self.pin[1], 100)]

    def start(self):
        if self.speed > 0 :
            self.pwm[0].start(self.speed)
            self.pwm[1].start(0)
        else:
            self.pwm[0].start(0)
            self.pwm[1].start(-self.speed)

    def stop(self):
        self.pwm[0].stop()
        self.pwm[1].stop()
            
    def speed(self, spd):
        self.speed = spd
        self.start()
        
if __function__ ==  __main__:
    

# Define GPIO signals to use
# Physical pins 12,16,18,22 -> GPIO[18,23,24,25]
# [GPIO18:INT1, GPIO23:INT2, GPIO24:INT3, GPIO25:INT4]
motor = {
    'right' : {
		1 : 18, 
		2 : 23
	},
    'left'  : {
		1 : 24, 
		2 : 25
	}
}

def init():
    global motor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor['right'][1], GPIO.OUT)
    GPIO.setup(motor['right'][2], GPIO.OUT)
    GPIO.setup(motor['left'][1], GPIO.OUT)
    GPIO.setup(motor['left'][2], GPIO.OUT)
    motor['right']['P'] = {
        1 : GPIO.PWM(motor['right'][1], 100),
        2 : GPIO.PWM(motor['right'][2], 100)
    }
    motor['left']['P'] = {
        1 : GPIO.PWM(motor['left'][1], 100),
        2 : GPIO.PWM(motor['left'][2], 100)
    }

# speed: 0 ~ 100 
def speed(m, s):
    if s > 0:
        m['P'][1].ChangeDutyCycle(s)
        m['P'][2].ChangeDutyCycle(0)
    else:
        m['P'][1].ChangeDutyCycle(0)
        m['P'][2].ChangeDutyCycle(-s)

def start():
    global motor
    motor['right']['P'][1].start()
    motor['right']['P'][2].start()
    motor['left']['P'][1].start()
    motor['left']['P'][2].start()

def stop():
    global motor
    motor['right']['P'][1].stop()
    motor['right']['P'][2].stop()
    motor['left']['P'][1].stop()
    motor['left']['P'][2].stop()

    
def stand-turn():



