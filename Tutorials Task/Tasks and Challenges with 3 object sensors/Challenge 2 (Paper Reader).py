"""
Challenge : 2
Create a Paper Size reader, where you need to place the paper on Reader 
and Reader will tell you its size whether it is A4, A5 or A6 size

1.A4 Size Paper = 0 1 0 
2.A5 Size Paper = 1 0 1
3.A6 Size Paper = 0 1 1
"""

# Importing Libraries
from Phygital_v0 import Phygital_v0 as pyro
import pygame 


#Pin Intialition 
pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

# #Communication Initialization
pyro.init('COM10')

#Source Code
while True:        
    try:
       data_OBJ_S_1=pyro.dRead('A3')
       data_OBJ_S_2=pyro.dRead('A4')
       data_OBJ_S_3=pyro.dRead('A5')
        
       if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 1 and data_OBJ_S_3 == 0:
           print("IT IS A4 SIZRE PAPER")
            
       if data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 1:
           print("IT IS A5 SIZE PAPER")
            
       if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 1 and data_OBJ_S_3 == 1: 
           print("IT IS A6 SIZE PAPER")      
           
      
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break

    
print("Closing")

                
