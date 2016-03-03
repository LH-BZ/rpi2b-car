# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 12,16,18,22 -> GPIO[18,23,24,25]
# [GPIO18:INT1, GPIO23:INT2, GPIO24:INT3, GPIO25:INT4]
motor = {
    "right" : {1 : 18, 2 : 23},
    "left"  : {1 : 24, 2 : 25}}

def motor_init():
    global motor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor["right"][1], GPIO.OUT)
    GPIO.setup(motor["right"][2], GPIO.OUT)
    GPIO.setup(motor["left"][1], GPIO.OUT)
    GPIO.setup(motor["left"][2], GPIO.OUT)

    motor["right"]["P"] = {
        1 : GPIO.PWM(motor["right"][1], 100),
        2 : GPIO.PWM(motor["right"][2], 100)}
    motor["left"]["P"] = {
        1 : GPIO.PWM(motor["left"][1], 100),
        2 : GPIO.PWM(motor["left"][2], 100)}

def motor_speed(m, s):
    if s > 0:
        m["P"][1].ChangeDutyCycle(s)
        m["P"][2].ChangeDutyCycle(0)
    else:
        m["P"][1].ChangeDutyCycle(0)
        m["P"][2].ChangeDutyCycle(-s)

def motor_start():
    global motor
    motor["right"]["P"][1].start()
    motor["right"]["P"][2].start()
    motor["left"]["P"][1].start()
    motor["left"]["P"][2].start()

def motor_stop():
    global motor
    motor["right"]["P"][1].stop()
    motor["right"]["P"][2].stop()
    motor["left"]["P"][1].stop()
    motor["left"]["P"][2].stop()

    
# def stand-turn():



