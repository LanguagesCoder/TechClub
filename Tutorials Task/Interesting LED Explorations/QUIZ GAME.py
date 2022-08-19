
"""
1. QUIZ Game :
Create a quiz game. In this game, whether user answer is 
correct or wrong will be shown by LEDs and Score will be shown 
by 3 LEDs (as 3 Stars,2 Stars, 1Star).
"""
from Phygital_v0 import Phygital_v0 as pyro
import time
pyro.pinMode("A0","dOutput")
pyro.pinMode("A1","dOutput")
pyro.pinMode("A2","dOutput")
pyro.pinMode("A3","dOutput")
pyro.pinMode("A4","dOutput")


# pyro.init("COM10")
while True :
    START = int(input("TO START PRESS 1:"))
    if START == 1:
        print("THERE WOULD BE  QUESTIONS")
        print(" ")
        print("IF THE RED LED GLOWS THEN YOUR ANSWER IS WRONG")
        print(" ")
        print("IF THE BLUE LED GLOWSTHEN YOUR ANSWER IS RIGHT")
        print(" ")
        print(" ")
        print("QUESTION 1")
        print("WHAT WAS THE YEAR OF TITANIC SINK ON 15 APRIL?")
        print(" ")
        print("OPTIONS")
        print("A:1916")
        print("B:1927")
        print("C:1912")
        print("D:1985")
        Q1 = input("ENTER YOUR ANSWER(IN CAPITAL LETTERS):")    
        if Q1 == 'C':
            Q1 = 5
            pyro.dWrite('A3',1)
            pyro.dWrite('A0',1)
            time.sleep (2)
            pyro.dWrite('A3',0)
            time.sleep(2)
        elif Q1 == 'A' and Q1 == 'B' and Q1 == 'D':
             pyro.dWrite('A4',1)
             time.sleep(2)
             pyro.dWrite('A4',0)
            
        print(" ")
        print(" ")
        print("QUESTION 2")
        print("WHICH YEAR WAS THE FIRST TONKA TRUCK MADE?")
        print(" ")
        print("OPTIONS")
        print("A:1947")
        print("B:1954")
        print("C:1975")
        print("D:1996")
        Q2 = input("ENTER YOUR ANSWER(IN CAPITAL LETTERS):")    
        if Q2 == 'A':
            Q2 = 6
            pyro.dWrite('A3',1)
            pyro.dWrite('A1',1)
            time.sleep (2)
            pyro.dWrite('A3',0)
            time.sleep(2)
        elif Q1 == 'C' and Q1 == 'B' and Q1 == 'D':
             pyro.dWrite('A4',1)
             time.sleep(2)
             pyro.dWrite('A4',0)
        
        
        print(" ")
        print(" ")
        print("QUESTION 3")
        print("IN WHICH YEAR 'PETER DURAND' MADE THE TIN CAN FOER PRESERVING FOOD?")
        print(" ")
        print("OPTIONS")
        print("A:1947")
        print("B:1954")
        print("C:1810")
        print("D:1720")
        Q3 = input("ENTER YOUR ANSWER(IN CAPITAL LETTERS):")    
        if Q3 == 'C':
            Q3 = 7
            pyro.dWrite('A3',1)
            pyro.dWrite('A2',1)
            time.sleep (2)
            pyro.dWrite('A3',0)
            time.sleep(2)
        elif Q1 == 'A' and Q1 == 'B' and Q1 == 'D':
             pyro.dWrite('A4',1)
             time.sleep(2)
             pyro.dWrite('A4',0)
        
        