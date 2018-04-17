#  MBTechWorks.com 2016
#  Pulse Width Modulation (PWM) demo to cycle brightness of an LED

import RPi.GPIO as GPIO   # Import the GPIO library.
import time								# Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use 
                          # Broadcom SOC channel names.

GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(12, 1000)   # Initialize PWM on pwmPin 100Hz frequency

exit=False
while exit==False:
    # main loop of program
    fval=float(input("0.1 - 100 choose start value(%): "))
    stp=int(input("Step size (0-100): "))
    while stp > 100:
        stp=int(input("Enter value 0-100: "))
    speed=float(input("Increment speed (s): "))
    print (fval)

    pwm.start(fval)       
    i=int(fval*10)                           
    for i in range(i, 1001, stp):        
        fval=float(i)/10
        pwm.ChangeDutyCycle(fval)
        time.sleep(speed)               
        print("% Duty: {0} Inc: {1}%/s".format(fval,stp/10/speed))
    var=input("Enter to continue, q to quit...")
    if var == "q":
        exit=True

pwm.stop()
GPIO.cleanup()                
