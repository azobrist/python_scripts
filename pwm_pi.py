#!/usr/bin/env python3
#  MBTechWorks.com 2016
#  Pulse Width Modulation (PWM) demo to cycle brightness of an LED

#import RPi.GPIO as GPIO   # Import the GPIO library.
import time								# Import time library

#GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use 
                          # Broadcom SOC channel names.

#GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
#pwm = GPIO.PWM(12, 1000)   # Initialize PWM on pwmPin 100Hz frequency
import pigpio

pi = pigpio.pi()
if not pi.connected:
    exit(0)

def set_pwm(per):
    pi.hardware_PWM(18,10000,int(per*10000))

exit=False
while exit==False:
    # main loop of program
    fval=float(input("0.1 - 100 choose start value(%): "))
    stp=int(input("Step size (1/1000): "))
    while stp > 100:
        stp=int(input("Enter value 0-100: "))
    #print (fval,stp,speed)

#    set_pwm(fval)       
    i=int(fval*10)
    if stp != 0:
        speed=float(input("Increment speed (s): "))
        for i in range(i, 1001, stp):        
            fval=float(i)/10
            set_pwm(fval)
            print("% Duty: {0} Inc: {1}%/s".format(fval,stp/speed))
            time.sleep(speed)
            #set_pwm(0)
            #input("Enter to continue...")
        time.sleep(1)
        set_pwm(0)
    else:
        set_pwm(fval)
        print("% Duty: {0}".format(fval)) 
    var=input("Enter to continue, q to quit...")
    if var == "q":
        exit=True

pi.stop()         
