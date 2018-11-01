#!/usr/bin/python3
#1d-mol.py
#Jeu du plus ou du moins
#Antoine Nicolleau

#Importation
import random
import sys
import signal

#Fonction permettant de quitter le jeu et de donner la réponse
def endGame(): 
    print("Perdu ! La solution était " + str(rdm) + ". A Bientôt ! ")
    sys.exit(0)
    return

# Fonction pour quitter joliement avec CTRL+C
def leaver (sig, frame):
    print('Tu as fait CTRL+C, la soltuion était ' + str(rdm))
    sys.exit(0)
   


signal.signal(signal.SIGINT, leaver)

# Initialisation du nombre random entre 1 et 100 
# et de la variable qui va contenir la saisie utilisateur
rdm = random.randint(1,100)
# print (rdm)
nbuser =input('Saisir un nombre entre 1 et 100 ? ')

# Tant que ma saisie utilisateur est différente de mon nombre rdm,
#boucler jusqu'à ce que l'utilisateur trouve le nombre.
while str(nbuser) != str(rdm):
    
    # Si le nombre entré est égal à q, cela quitte le jeu
    if str(nbuser) == 'q':
        endGame()
    
    # Si ce n'est pas un nombre 
    elif str(nbuser) is not int :
        print("Ceci n'est pas un nombre, veuillez réessayer")
    
    elif int(nbuser) < int(rdm):
        print("C'est plus")
    
    elif int(nbuser) > int(rdm) and int(nbuser) > 0 and int(nbuser) < 100:
        print("C'est moins")
    
    elif int(nbuser) < 0 or int(nbuser) > 100: 
        print("Saisissez un nombre valable entre 1 et 100")

    nbuser = input('Saisir un nombre entre 1 et 100 ? ')

if int(nbuser) == int(rdm):
    print("Bravo tu as gagné ! La solution était bien " + nbuser + ". A Bientôt !")

