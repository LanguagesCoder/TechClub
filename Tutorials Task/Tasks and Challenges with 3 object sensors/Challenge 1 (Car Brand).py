"""
Challenge : 1
Create a Game in which there would be cards for Logos of Car brands 
and the Car Models would be displayed randomly on screen, user needs 
to place the correct Logo card for the Car displayed.

1.Hyundai =       1 0 0 
2.Maruti Suzuki = 0 1 1
3.Ford =          0 0 1

"""
#Importing Libraies
from Phygital_v0 import Phygital_v0 as pyro
import time
import pygame
import random

#Pin Initialization
pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

#Library/Communication Initialization
pyro.init("COM10")
pygame.init()

#Setting Up The Window
Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))
#Variables
num = random.randint(1,3)

#Loading Images
ScreenImage = pygame.image.load("Images/Background Image.png")
Verna = pygame.image.load("Images/Verna.png")
Swift = pygame.image.load("Images/Swift.png")
Ecosport = pygame.image.load("Images/Ecosport.png")

#Showing The Background Image
screen.blit(ScreenImage,(0,0))

#Printing Randome Number And Asking For That Number 
print(num)
NUMBER_ASK = int(input("ENTER THE NUMBER IN THE CONSOLE YOU HAVE GOT :"))

#Source Code
while True :
    try:
        #Starting the sensor for sensing
        data_OBJ_S_1=pyro.dRead('A3')
        data_OBJ_S_2=pyro.dRead('A4')
        data_OBJ_S_3=pyro.dRead('A5')
        
        #Checking Weather The Card That is Placed is Correct Or Not (Hyundai)
        if NUMBER_ASK == 1:
            screen.blit(Verna,(0,0))
            if data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 0:
                print("CORRECT")
            if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 1 and data_OBJ_S_3 == 1:
                print("WRONG")
            if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 1:
                print("WRONG")    
       
        #Checking Weather The Card That is Placed is Correct Or Not (Maruti Suzuki)
        elif NUMBER_ASK == 2:
            screen.blit(Swift,(0,0))    
            if data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 0:
                print("WRONG")
            if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 1 and data_OBJ_S_3 == 1:
                print("CORRECT")
            if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 1:
                print("WRONG")           
        
        #Checking Weather The Card That is Placed is Correct Or Not (Ford)
        elif NUMBER_ASK == 3:   
            screen.blit(Ecosport,(0,0))
            if data_OBJ_S_1 == 1 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 0:
                print("WRONG")
            if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 1 and data_OBJ_S_3 == 1:
                print("WRONG")
            if data_OBJ_S_1 == 0 and data_OBJ_S_2 == 0 and data_OBJ_S_3 == 1:
                print("CORRECT")   
        
        #Closing The pygame Window 
        EventStatus="None"
    
        pygame.display.update()
        
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                EventStatus="Quit"
                break
           
            
        if EventStatus == "Quit":
            break        
    
    #Closing The Communictaion Between The Computer And Hardware    
    except:
        if KeyboardInterrupt:
            pyro.close()
            break

    
print("Closing")

