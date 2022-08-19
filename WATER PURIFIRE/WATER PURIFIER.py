"""
WATER PURIFIER
"""

from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A0","dOutput")
pyro.pinMode("A1","dOutput")
pyro.pinMode("A2","dOutput")
pyro.pinMode("A3","dOutput")
pyro.pinMode("A4","dOutput")
pyro.pinMode("A5","dOutput")

pyro.init("COM10")

START_AND_DIGNO = int(input("ENTER 10 TO START THE PRIFIER AND THE SURVEY:")) 





if START_AND_DIGNO == 10:
    print("'1' INDICATES THE PROBLEM ")
    print("'0' INDICATES NO PROBLEM")
     
    
    PR1 = int(input("1.OUTLET PIPE CHOCKED:"))
    PR2 = int(input("2.POWER OFF:"))
    PR3 = int(input("3.WATER TANK EMPTY:"))
    PR4 = int(input("4.PIPE BROKEN:"))
    PR5 = int(input("5.PURIFER RODS ARE EXHAUSTED:"))
    PR6 = int(input("6.THERE IS NOWATER SOURCE:"))
    
    while True:        
        try:
            if PR1 == 1:
                PR1 =7
                pyro.dWrite('A0',1)
            if PR1 == 0:
                PR1 =7    
                pyro.dWrite('A0',0)
                
            if PR2 == 1:
                PR2 =8
                pyro.dWrite('A1',1)
            if PR2 == 0:
                PR2 =8    
                pyro.dWrite('A1',0)
                    
            if PR3 == 1:
                PR3 =9
                pyro.dWrite('A2',1)
            if PR3 == 0:
                PR3 =9    
                pyro.dWrite('A2',0)
                    
            if PR4 == 1:
                PR4 =10
                pyro.dWrite('A3',1)
            if PR4 == 0:
                PR4 =10
                pyro.dWrite('A3',0)
                
            if PR5 == 1:
                PR5 =11
                pyro.dWrite('A4',1)
            if PR5 == 0:
                PR5 =11
                pyro.dWrite('A4',0)
                    
            if PR6 == 1:
                PR6 =12
                pyro.dWrite('A5',1)    
            if PR6 == 0:
                PR6 =12
                pyro.dWrite('A5',0)
                
    
        except:
            if KeyboardInterrupt:
                pyro.close()
                break
        

print("Closed the Connection!!")



        
        
        
        

