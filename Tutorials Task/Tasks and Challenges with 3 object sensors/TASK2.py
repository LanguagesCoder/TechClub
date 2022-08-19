from Phygital_v0 import Phygital_v0 as pyro

pyro.pinMode('A3','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A5','dInput')

pyro.init("COM10")

count_OBJ_S_1 = 0
count_OBJ_S_2 = 0
count_OBJ_S_3 = 0
while True :
    try:
        data_OBJ_S_1=pyro.dRead('A3')
        data_OBJ_S_2=pyro.dRead('A4')
        data_OBJ_S_3=pyro.dRead('A5')
        
        if data_OBJ_S_1==0:# Object Sensed
            while data_OBJ_S_1==0 :
                data=pyro.dRead('A3')
                count_OBJ_S_1 = count_OBJ_S_1 = 0+1
            
            
        if data_OBJ_S_2==0:# Object Sensed
            while data_OBJ_S_2==0 :
                data=pyro.dRead('A4')
                count_OBJ_S_2 = count_OBJ_S_2 = 0+1
            
            
        if data_OBJ_S_3==0:# Object Sensed
            while data_OBJ_S_3==0 :
                data=pyro.dRead('A5')
                count_OBJ_S_3 = count_OBJ_S_3 = 0+1  
            
        print("OBJ 1 " + str(count_OBJ_S_1) + "OBJ 2 " + str(count_OBJ_S_2) + "OBJ 3 " + str(count_OBJ_S_3))    

       
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break

    
print("Closing")
