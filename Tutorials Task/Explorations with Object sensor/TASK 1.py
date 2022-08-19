# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:24:31 2020

@author: sir
"""
from Phygital_v0 import Phygital_v0 as pyro
# import time
pyro.pinMode('A4','dInput')
# pyro.pinMode('A0','dOutput')
# pyro.pinMode('A1','dOutput')

pyro.init('COM10')


while True :
    try:
        data = pyro.dRead('A4')
        print("SENSOR STATE :"+ str (data))
        
        
        if data == 0:
 
            print("OBJECT SENSED")
            # pyro.dWrite('A0',1)
            # time.sleep(1)
            # pyro.dWrite('A1',1)
        else:
           
            print("NO OBJECT")
            # pyro.dWrite('A0',0)
            # pyro.dWrite('A1',0)
            
                
    except:
        if KeyboardInterrupt:
            pyro.close()
        
            break
print("Closed the Connection!!")


























