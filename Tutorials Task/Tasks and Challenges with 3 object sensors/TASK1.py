# Importing Libraries
from Phygital_v0 import Phygital_v0 as pyro
import pygame 


#Pin Intialition 
pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

# #Communication Initialization
pyro.init('COM10')


#Setting up the pygame window
Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))

#Loading Images

ScreenImage = pygame.image.load("Images/Background Image.png")
Hand = pygame.image.load("Images/Hand.png")
Scale= pygame.image.load("Images/Ruler.png")
White_Object = pygame.image.load("Images/White Object.png")
screen.blit(ScreenImage,(0,0))

#Variables


ASK = input("CAN WE START :")
if ASK == 'YES':      
    print("YOU CAN USE:")
    print("Object Sensor 1 : Hand")	
    print("Object Sensor 2 : Scale")
    print("Object Sensor 3 : White Object")
while True:        
    try:
       data_OBJ_S_1=pyro.dRead('A3')
       data_OBJ_S_2=pyro.dRead('A4')
       data_OBJ_S_3=pyro.dRead('A5')
        
       if data_OBJ_S_1 == 0:
            screen.blit(Hand,(0,0))
            
       if data_OBJ_S_2 == 0:
           screen.blit(Scale,(0,0))
            
       if data_OBJ_S_3 == 0:
            screen.blit(White_Object,(0,0))    
       EventStatus="None"
    
       pygame.display.update()
        
         
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                EventStatus="Quit"
                break
           
            
       if EventStatus == "Quit":
            break        
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break

    
print("Closing")

                

