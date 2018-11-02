#!/usr/bin/python3
#2a-mol.py
#Jeu du plus ou du moins en démon
#Antoine Nicolleau

#Importation
import random
import sys

#Instanciation
rdm = random.randint(1,100)
nbuser = sys.stdout
filetest = '2atest'
welcome = 'Bonjour et bienvenu dans ce jeu du plus ou du moins. Pour commencer le jeu, entrer un nombre'

filetmp = open(filetest, "w")
filetmp.write(welcome)





# Tant que ma saisie utilisateur est différente de mon nombre rdm,
#boucler jusqu'à ce que l'utilisateur trouve le nombre.
    
    # Si ce n'est pas un nombre 
if str(nbuser) is not int :
        print("Ceci n'est pas un nombre, veuillez réessayer")
    
elif int(nbuser) < int(rdm):
        print("C'est plus")
    
elif int(nbuser) > int(rdm) and int(nbuser) > 0 and int(nbuser) < 100:
        print("C'est moins")
    
elif int(nbuser) < 0 or int(nbuser) > 100: 
        print("Saisissez un nombre valable entre 1 et 100")


elif int(nbuser) == int(rdm):
    print("Bravo tu as gagné ! La solution était bien " + nbuser + ". A Bientôt !")

