#!/usr/bin/python3
#2b-auto.py
#Script qui résout le plus ou moins dans 2a-mol.py
#Antoine Nicolleau


#importantion
import os
import time

#Initialisation
read_file = "2atest.txt"
high_number = 101
low_number = -1
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
    print(int(guessed_number))
    print("high_number : " + str(high_number))
    print("low_number : " + str(low_number))

    gamefile = open(read_file, "r")
    compteur = 0

    

    for line in gamefile.readlines():
        compteur += 1
        if compteur == 1:
            indice = line
            print("line : " + indice)
            

            if "plus" in indice:
                print("ça passe 2")
                low_number = int(guessed_number)

            elif "moins" in indice:
                high_number = int(guessed_number)

            elif "gagné" in indice:
                print('C\'est gagné, le nombre était ' + str(guessed_number))
                success = True
        

    guessed_number = (int(high_number) + int(low_number)) / 2
    append(read_file, str(guessed_number))

    time.sleep(2)
    gamefile.close()