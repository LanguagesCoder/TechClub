"""
2. Connect two LEDs , LED1 - A0, LED2 - A1,  put both of them on
"""

from Phygital_v0 import Phygital_v0 as pyro

pyro.pinMode("A0","dOutput")
pyro.pinMode("A1","dOutput")

pyro.init("COM10")

while True:
    try:
        pyro.dWrite('A0',1)
        pyro.dWrite('A1',1)
        
    except:
         if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")