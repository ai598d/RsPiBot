# import libraries
import RPi.GPIO as GPIO
import time
#import distance_sensor as ds

# setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


#loop

while(True):
        GPIO.output(23,True)
        GPIO.output(18, True)
        time.sleep(0.000010)
        GPIO.output(18, False)
        time.sleep(0.000010)
        #print(ds.distance())
        
         #   print("MOTOR stopped by user")
          #  GPIO.cleanup()

