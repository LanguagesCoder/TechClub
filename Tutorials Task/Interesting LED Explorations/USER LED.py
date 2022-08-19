"""
1. Create a LED control panel where you need to take the LED Number as Input and the LED State as input. You need to apply the state input by user to the LED.

Expected Output: Enter the LED Number: 3

Enter LED State: on

In this case you need to put ON LED 3
"""
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A0","dOutput")
pyro.pinMode("A1","dOutput")
pyro.pinMode("A2","dOutput")
pyro.pinMode("A3","dOutput")
pyro.pinMode("A4","dOutput")


pyro.init("COM10")

while True :
    try:
        LED_NUM = int(input("ENTER THE LED NUMBER WHICH YOU WANT (FROM 1 TO 5 NUMBERS ONLY):"))
        LED_STATE = input("ENTER 'O' TO ON THE LED:")
        print("LED WOULD BE ON FOR ONLY 10 SECONDS.")
        
        if LED_NUM == 1 and LED_STATE == 'O':
            LED_NUM = 6
            LED_STATE = 6
            pyro.dWrite('A0',1)
            time.sleep(10)
            pyro.dWrite('A0',0)
            
        if LED_NUM == 2 and LED_STATE == 'O':
            LED_NUM = 7
            LED_STATE = 7
            pyro.dWrite('A1',1)
            time.sleep(10)
            pyro.dWrite('A1',0)
            
        if LED_NUM == 3 and LED_STATE == 'O':
            LED_NUM = 8
            LED_STATE = 8
            pyro.dWrite('A2',1)
            time.sleep(10)
            pyro.dWrite('A2',0)
            
        if LED_NUM == 4 and LED_STATE == 'O':
            LED_NUM = 9
            LED_STATE = 9
            pyro.dWrite('A3',1)
            time.sleep(10)
            pyro.dWrite('A3',0)    
            
        if LED_NUM == 5 and LED_STATE == 'O':
            LED_NUM = 10
            LED_STATE = 10
            pyro.dWrite('A4',1)
            time.sleep(10)
            pyro.dWrite('A4',0)    
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
        print("HAVE A NICE DAY")
print("Closed the Connection!!")        