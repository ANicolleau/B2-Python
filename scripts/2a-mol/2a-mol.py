#!/usr/bin/python3
#2a-mol.py
#Jeu du plus ou du moins en démon
#Antoine Nicolleau

#Importation
import random
import sys
import time

#Instanciation
rdm = random.randint(1,100)
nbuser = -1
filetest = '2atest.txt'
welcome = 'Bonjour et bienvenu dans ce jeu du plus ou du moins. Pour commencer le jeu, entrez un nombre entre 0 et 100 sur la 2e ligne'
plus = 'C\'est plus'
moins = 'C\'est moins'
win = 'C\'est gagné, le nombre était bien : '
rejouer = 'Entrez un nombre entre 1 et 100'


# fonction qui me permet d'écrire dans les fichiers
def write(file,msg):
        filetmp = open(file, "w")
        filetmp.write(msg)
        filetmp.close

write(filetest, welcome)


# Tant que ma saisie utilisateur est différente de mon nombre rdm,
#boucler jusqu'à ce que l'utilisateur trouve le nombre.
    
    # Si ce n'est pas un nombre 
while int(nbuser) != int(rdm):
        gamefile = open(filetest, "r")
        compteur = 0
        for line in gamefile.readlines():
                compteur += 1
                if compteur == 2:
                        nbuser = line

                        if int(nbuser) < int(rdm):
                                write(filetest,plus)
                        
                        elif int(nbuser) > int(rdm) :
                                write(filetest, moins)
                        
                        elif int(nbuser) < 0 or int(nbuser) > 100: 
                               write(filetest, rejouer)

                        elif int(nbuser) == int(rdm):
                                write(filetest, win)

        gamefile.close()
        time.sleep(3)
