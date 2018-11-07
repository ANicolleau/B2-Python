#!/usr/bin/python3
#2b-auto.py
#Script qui résout le plus ou moins dans 2a-mol.py
#Antoine Nicolleau


#importantion
import os
import time

#Initialisation
read_file = "2atest.txt"
high_number = 100
low_number = 0
guessed_number = 0
success = False
indice = ''

#Fonction lançant le jeu 
def write(file, msg):
    filetmp = open(file, "w")
    filetmp.write(msg)
    filetmp.close()

def append(file, msg):
    filetmp = open(file, "a")
    filetmp.write("\n" + msg)
    filetmp.close()

print("Résolution du jeu en cours")

# résoudre le jeu
while (success == False):
    guessed_number = (float(high_number) + float(low_number)) / 2
    append(read_file, str(guessed_number))
    print(str(guessed_number))
    print("high_number : " + str(high_number))
    print("low_number : " + str(low_number))

    gamefile = open(read_file, "r")
    compteur = 0

    

    for line in gamefile.readlines():
        compteur += 1
        if compteur == 1:
            indice = line
            print("line : " + line)
            

    if indice == "plus":
        low_number = float(guessed_number)

    elif indice == "moins": 
        high_number = float(guessed_number)

    elif indice == "gagné":
        print('C\'est gagné, le nombre était ' + str(guessed_number))
        success = True
        
    gamefile.close()
    time.sleep(2)