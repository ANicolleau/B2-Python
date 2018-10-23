#!/usr/bin/python3
#1d-mol.py
#Jeu du plus ou du moins
#Antoine Nicolleau
#23 oct 2018

# Initialisation du nombre random entre 1 et 100 
# et de la variable qui va contenir la saisie utilisateur
import random
rdm = random.randint(1,100)

print (rdm)

nbuser =input('Saisir un nombre entre 1 et 100 ? ')
# Tant que ma saisie utilisateur est différente de mon nombre rdm,
#boucler jusqu'à ce que l'utilisateur trouve le nombre.
while int(nbuser) != int(rdm) or str(nbuser) != q:
    
    if int(nbuser) < int(rdm):
        print("C'est plus")
    
    elif int(nbuser) > int(rdm) and int(nbuser) > 0 and int(nbuser) < 100:
        print("C'est moins")
    
    elif int(nbuser) < 0 or int(nbuser) > 100: 
        print("Saisissez un nombre valable entre 1 et 100")

    nbuser = input('Saisir un nombre entre 1 et 100 ? ')

if int(nbuser) == int(rdm):
    print("Bravo tu as gagné ! La solution était bien " + nbuser + ". A Bientôt !")
