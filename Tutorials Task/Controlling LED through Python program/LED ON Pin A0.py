"""
1. Connect the LED at Pin A2 and put it On
"""

"""Library"""
from Phygital_v0 import Phygital_v0 as pyro

"""Pin Initialization"""
pyro.pinMode('A2','dOutput')

"""Init"""
pyro.init("COM10")

"""LED ON"""
 
while True:
    try:
        pyro.dWrite('A2',1)#LED ON
          
        
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")

