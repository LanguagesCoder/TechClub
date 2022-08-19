
"""
2. Create a pattern shown in following videos:
"""
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A0","dOutput")
pyro.pinMode("A1","dOutput")
pyro.pinMode("A2","dOutput")
pyro.pinMode("A3","dOutput")
pyro.pinMode("A4","dOutput")


pyro.init("COM10")



       
for i in range(6):
    pyro.dWrite('A0',1)
    time.sleep(0.5)
    pyro.dWrite('A0',0)
    time.sleep(0.5)
    pyro.dWrite('A0',1)

time.sleep(1)
    
for i in range(6):
    pyro.dWrite('A1',1)
    time.sleep(0.5)
    pyro.dWrite('A1',0)
    time.sleep(0.5)
    pyro.dWrite('A1',1)

time.sleep(1)

for i in range(6):
    pyro.dWrite('A2',1)
    time.sleep(0.5)
    pyro.dWrite('A2',0)
    time.sleep(0.5)
    pyro.dWrite('A2',1)

time.sleep(1)

for i in range(6):
    pyro.dWrite('A3',1)
    time.sleep(0.5)
    pyro.dWrite('A3',0)
    time.sleep(0.5)
    pyro.dWrite('A3',1)

time.sleep(1)

for i in range(6):
    pyro.dWrite('A4',1)
    time.sleep(0.5)
    pyro.dWrite('A4',0)
    time.sleep(0.5)
    pyro.dWrite('A4',1)    
            
time.sleep(1)        

        


        
print("Closed the Connection!!")


