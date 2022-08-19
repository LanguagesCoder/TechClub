"""
5. Make LED blink with rate ON Time- 2 Sec, OFF-Time-500 MilliSec. Connect LED at pin A5
"""

from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A5","dOutput")

pyro.init("COM10")

while True:
    try:
        pyro.dWrite('A5',1)
        time.sleep(2)
        pyro.dWrite('A5',0)
        time.sleep(0.5)
        
        
    except:
         if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")
