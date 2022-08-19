
"""
3. Make the LED Blink , LED connected at Pin A4
"""
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A4","dOutput")

pyro.init("COM10")

while True:
    try:
        pyro.dWrite('A4',1)
        time.sleep(1)
        pyro.dWrite('A4',0)
        time.sleep(1)
        
        
    except:
         if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")