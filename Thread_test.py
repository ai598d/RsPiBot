from threading import Thread
import time

global cycle
cycle = 0.0

class Hello5Program:
    def __init__(self):
        self._running= True
        
    def terminate (self):
        self._running= False
        
    def run(self):
        global cycle
        while self._running:
            time.sleep(5)  # five sec delay
            cycle = cycle+1
            print("5 sec thread cycle+1 -",cycle)

class Hello2Porgram:
    def __init__(self):
        self._running= True
        
    def terminate (self):
        self._running= False
        
    def run(self):
        global cycle
        while self._running:
            time.sleep(2) # 2 sec delay
            cycle = cycle+.5
            print("2 sec thread cycle+1 -",cycle)
            
            
Fivesec = Hello5Program() # create class

FivesecThread = Thread(target=Fivesec.run) # create thred

FivesecThread.start()  # start the thread


Twosec = Hello2Program() # create class

TwosecThread = Thread(target=Twosec.run) # create thred

TwosecThread.start()  # start the thread

    
    
    
    
    
    
    
    
    
    
            

            