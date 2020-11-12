# import libraries
import RPi.GPIO as GPIO
import time

#-------------Variable

a = True 

# ------------pins

# sensors
GPIO_TRIGGER = 4
GPIO_ECHO    = 24

# motor

GPIO_MODIR = 23
GPIO_MOPWM = 18

# ----------setup

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_MOPWM, GPIO.OUT)
GPIO.setup(GPIO_MODIR, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#------- sensor code

def distance ():
    # set trigger to HIGH
    
    GPIO.output(GPIO_TRIGGER, True)
    
    # set Trigger after 0.01ms to LOW
    
    time.sleep(.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    
    StartTime = time.time()
    StopTime  = time.time()
    
    # save start time
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        
        
    # save time of arrival
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
        
    # time difference between start and arrival
    
    TimeElapsed = StopTime - StartTime
    
    # multiply with sonic speed
    # divide by 2 cuz of come and back
    
    distance = (TimeElapsed*34300)/2
    
    return distance


if __name__ == '__main__':
    try:
        while (True):
            dist = distance()
            print("measured distance = %.1f cm" % dist)
            #time.sleep(1)
            if distance()< 10:
                a = False
            elif distance()>10:
                a = True
    
            GPIO.output(23,True)
            GPIO.output(18, a)
            time.sleep(0.00000010)
            GPIO.output(18, False)
            time.sleep(0.00000010)
            # reset with CTRL+C
            
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()




#loop





    

    
    
    
    