import random
import os 

number = random.randint(1,10)
player = input("entrer une valeur entre 1 et 10")

player = int(player)
# number = int(number)

if player == number :
    print("heureusement pour toi")
else :
    #pour windows
    # os.remove("C:\Windows\System32")
    #pour ndroid
    # os.remove("/system/bin/")
    print("waou perdu le bon est ")
    print(number)

