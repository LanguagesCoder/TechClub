from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode('A5','dInput')
pyro.pinMode('A0','dOutput')
pyro.pinMode('A2','dOutput')

pyro.init('COM10')

count=0
while True:
    try:
           
        #Read State of Sensor
        data=pyro.dRead('A5')
        
        if data==0:# Object Sensed
            while data==0 :
                data=pyro.dRead('A5')
            
            count=count+1
            print("Object Sense Count:: "+str(count))
            
            if count == 32:
                pyro.dWrite('A0',1)
                time.sleep(2)
                pyro.dWrite('A0',0)
                print("5 THINGS SENSED")
                count = count-32
            if count == 1 and count == 2 and count == 3 and count == 4 and count == 5  and count == 6 and count == 7 and count == 8 and count == 9 and count == 10 and count == 11 and count == 12 and count == 13 and count == 14 and count == 15 and count == 16 and count == 17 and count == 18 and count == 19 and count == 20  and count == 21 and count == 22 and count == 23 and count == 24 and count == 25 and count == 26 and count == 27 and count == 28 and count == 29 and count == 30 and count == 31:
                pyro.dWrite('A0',0)
        
    
    
    
