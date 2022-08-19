"""
4. Make the LED blink with ON Time - 500 MilliSec, OFF-Time-500 MilliSec . Connect LED at pin A3
"""
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A3","dOutput")

pyro.init("COM10")

while True:
    try:
        pyro.dWrite('A3',1)
        time.sleep(0.5)
        pyro.dWrite('A3',0)
        time.sleep(0.5)
        
        
    except:
         if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")