
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A0","dOutput")
pyro.pinMode("A1","dOutput")
pyro.pinMode("A2","dOutput")
pyro.pinMode("A3","dOutput")
pyro.pinMode("A4","dOutput")


pyro.init("COM10")

while True :

    pyro.dWrite('A0',1)
    pyro.dWrite('A1',1)
    pyro.dWrite('A2',1)
    pyro.dWrite('A3',1)
    pyro.dWrite('A4',1)
    
    time.sleep(1)
    
    pyro.dWrite('A0',0)
    pyro.dWrite('A1',0)
    pyro.dWrite('A2',0)
    pyro.dWrite('A3',0)
    pyro.dWrite('A4',0)
    
    time.sleep(1)