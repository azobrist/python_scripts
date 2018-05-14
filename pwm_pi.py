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
    #ontime=0.5
    #offtime=0.5
    #offval=10
    #print("On Time: {0} Off Time: {1} Off value: {2}%\n".format(ontime,offtime,offval))
    #offval=input("Off time duty cycle(%): ")
    i=float(input("0.1 - 100 choose start value(%): "))
    st=int(input("Step size (1/10 of 1%, 10 - 100): "))
    while st > 100:
        st=int(input("Enter value 0-100: "))
    cnr=int(input("Enter % to begin rolloff(1-100): "))
    #kndiv=input("Enter divisor for step at rolloff: ")
    #knmult=input("Enter factor for dwel at rolloff: ")
    tt=0
    kndiv=10
    knmult=2

    x=int(i*10)
    if st != 0:
        speed=float(input("Enter dwell time / step (s): "))
        maxst = int(1000) - 50 #how many steps to get to 95% 
        cnrst = cnr * 10 + 1#set knee cap
        for x in range(x, cnrst, st):        
            i=float(x)/10
            set_pwm(i)
            tt += speed
            print("% Duty: {0} Inc: {1}% Time: {2:.6f}s".format(i,float(st)/10,tt))
            time.sleep(speed)
        st = int(st/kndiv)
        speed = speed*knmult
        print("Begin rolloff - Step size = {0}% Dwell = {1}s".format(float(st)/10,speed))
        for x in range(x, maxst, st):
            i=float(x)/10
            set_pwm(i)
            tt += speed
            print("% Duty: {0} Inc: {1}% Time: {2:.6f}s".format(i,float(st)/10,tt))
            time.sleep(speed)
        time.sleep(1)
        set_pwm(0)
    else:
        set_pwm(i)
        print("% Duty: {0}".format(i)) 
    var=input("Enter to continue, q to quit...")
    if var == "q":
        exit=True

pi.stop()         
