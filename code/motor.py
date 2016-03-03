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

def motor-init():
    global motor
    GPIO.setmode(GPIO.BCM)

    for k in motor:
        GPIO.setup(k[1], GPIO.OUT)
        GPIO.setup(k[2], GPIO.OUT)

        k["P"] = {
            1 : GPIO.PWM(k[1], 100),
            2 : GPIO.PWM(k[2], 100)}

# 0 ~ 100，实际上是调整PWM的占空比
def motor-speed(m， s):
    if s > 0:
        m["P"][1].ChangeDutyCycle(s)
        m["P"][2].ChangeDutyCycle(0)
    else:
        m["P"][1].ChangeDutyCycle(0)
        m["P"][2].ChangeDutyCycle(-s)

def motor-start():
    global motor
    for k in motor:
        k[P][1].start()
        k[P][2].start()

def stand-turn():


# Define advanced sequence
# as shown in manufacturers datasheet
SeqSinglePhase = [[1,0,0,0],
          [0,1,0,0],
          [0,0,1,0],
          [0,0,0,1]]

SeqFullDualPhase = [[1,1,0,0],
                [0,1,1,0],
                [0,0,1,1],
                [1,0,0,1]]

SeqHalfStep = [[1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,0,1,0],
           [0,0,1,1],
           [0,0,0,1],
           [1,0,0,1]]

# Select Sequence Mode
Seq = SeqSinglePhase

# 1 clockwise, -1 anti-clockwise
StepDir = 1

StepCount = len(Seq)

# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

# Initialise variables
if (StepDir == 1):
  StepCounter = 0
else:
  StepCounter = StepCount - 1

# Start main loop
Count = 1
while True:
  # Quit after 1 rotation 360 degree
  if (Count > 512 * StepCount):
    break
  print "Count %i" % Count
  Count += 1

  print "Step: %i" %(StepCounter)
  for pin in range(0, 4):
    xpin = StepPins[pin]
#    print pin
    if Seq[StepCounter][pin]!=0:
      print " %i *" %(pin)
      GPIO.output(xpin, True)
    else:
      print " %i -" %(pin)
      GPIO.output(xpin, False)

  StepCounter += StepDir

  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount - 1

  # Wait before moving on
  time.sleep(WaitTime)
