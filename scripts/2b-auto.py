#!/usr/bin/python3
#2b-auto.py
#Script qui résout le plus ou moins dans 2a-mol.py
#Antoine Nicolleau


#importantion
import os
import time

#Initialisation
read_file = "2atest.txt"
script_file = "2a-mol.py"
high_number = 100
low_number = 1
guessed_number = 0
win_number = -1
success = 0

#Fonction lançant le jeu 
def write(file,msg):
    filetmp = open(file, "w")
    filetmp.write(msg)
    filetmp.close()

print("Résolution du jeu en cours")

# résoudre le jeu
while (success == 0):
    guessed_number = (int(high_number) + int(low_number)) / 2
    gamefile = open(read_file, "r")
    compteur = 0
    
    for line in gamefile.readlines():
        compteur += 1
        gamefile.close()
        
        if compteur == 2:
            guessed_number = line
            write(read_file, str(guessed_number))

            if os.system('cat ' + script_file + ' | grep plus' ):
                low_number = int(guessed_number)

            elif os.system('cat ' + script_file + ' | grep moins' ): 
                high_number = int(guessed_number)

            elif os.system('cat ' + script_file + ' | grep gagné' ):
                print('C\'est gagné, le nombre était ' + int(guessed_number))
                success = 1  

        

    time.sleep(2)