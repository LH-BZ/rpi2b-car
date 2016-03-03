root@raspberrypi:/home/simba/src/rpi2b-car/code# python
Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import motor
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "motor.py", line 29
SyntaxError: Non-ASCII character '\xef' in file motor.py on line 29, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
>>> import motor
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "motor.py", line 29
SyntaxError: Non-ASCII character '\xef' in file motor.py on line 29, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
>>> import motor
>>> motor_init()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'motor_init' is not defined
>>> import motor as motor
>>> import motor as motor
>>> motor.motor_init()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "motor.py", line 22, in motor_init
    GPIO.setup(k[1], GPIO.OUT)
ValueError: Channel must be an integer or list/tuple of integers
>>> import motor as motor
>>> motor.motor_init()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "motor.py", line 22, in motor_init
    GPIO.setup(motor["right"][2], GPIO.OUT)
ValueError: Channel must be an integer or list/tuple of integers
>>> exit()
root@raspberrypi:/home/simba/src/rpi2b-car/code# python
Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import motor as motor
>>> motor.motor_init()
>>> motor.motor_speed(motor.motor["right"], 30)
>>> motor.motor_speed(motor.motor["left"], 30)
>>> motor.motor_start()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "motor.py", line 42, in motor_start
    motor["right"]["P"][1].start()
TypeError: function takes exactly 1 argument (0 given)
>>> import RPi.GPIO as GPIO
>>> GPIO.setmode(GPIO.BCM)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'GIO' is not defined
>>> GPIO.setmode(GPIO.BCM)
>>> GPIO.setup(23, GPIO.OUT)
>>> GPIO.setup(24, GPIO.OUT)
>>> GPIO.setup(25, GPIO.OUT)
>>> GPIO.setup(25, GPIO.OUT)
>>> p23 = GPIO.PWM(23, 100)
>>> p24 = GPIO.PWM(24, 100)
>>> p25 = GPIO.PWM(25, 100)
>>> p25 = GPIO.PWM(25, 100)
>>> p23.start(30);time.sleep(1);p23.stop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'time' is not defined
>>> p23.start(30);time.sleep(1);p23.stop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'time' is not defined
>>> import time
>>> time.sleep(1)
>>> p23.start(30);time.sleep(1);p23.stop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'slee'
>>> p23.start(30);time.sleep(1);p23.stop()
>>> p18.start(0)
>>> p23.start(100);p18.start(60);time.sleep(1);p18.start(100)
>>> p23.start(0);p18.start(0)
>>> p23.start(30);p24.start(30);time.sleep(2);p23.start(0);p24.start(0)
>>> p23.start(30);p24.start(30);time.sleep(5);p23.start(0);p24.start(0)
>>> p23.start(30);p24.start(30);time.sleep(5);p23.start(0);p24.start(0)
>>> p18.start(30);p25.start(30);time.sleep(1);p18.start(0);p25.start(0)
>>> p23.start(30);p24.start(30);time.sleep(2);p23.start(0);p24.start(0)
>>> p23.start(30);p25.start(30);time.sleep(3);p23.start(0);p25.start(0)
>>> p18.start(30);p24.start(30);time.sleep(3);p18.start(0);p24.start(0)
>>> p23.start(30);p25.start(30);time.sleep(3);p23.start(0);p25.start(0)
>>> p18.start(30);p24.start(30);time.sleep(3);p18.start(0);p24.start(0)
>>> p23.start(30);p25.start(30);time.sleep(3);p23.start(0);p25.start(0)
>>> p18.start(30);p24.start(30);time.sleep(3);p18.start(0);p24.start(0)
>>> p23.start(30);p25.start(30);time.sleep(3);p23.start(0);p25.start(0)
>>> p23.start(20);p25.start(20);time.sleep(3);p23.start(0);p25.start(0)
>>> p18.start(25);p24.start(25);time.sleep(3);p18.start(0);p24.start(0)
>>> 