
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode('A4','dInput')
pyro.pinMode('A0','dOutput')
pyro.pinMode('A2','dOutput')

pyro.init('COM10')

count=0
while True:
    try:
           
        #Read State of Sensor
        data=pyro.dRead('A4')
        
        if data==0:# Object Sensed
            while data==0 :
                data=pyro.dRead('A4')
            
            count=count+1
            print("Object Sense Count:: "+str(count))
            
            if count == 5:
                pyro.dWrite('A0',1)
                time.sleep(2)
                pyro.dWrite('A0',0)
                print("5 THINGS SENSED")
                count = count-5
            if count == 1 and count == 2 and count == 3 and count == 4:
                pyro.dWrite('A0',0)
        
    
    
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")