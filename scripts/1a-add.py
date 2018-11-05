#!/usr/bin/python3
#1a-add.py
#Demander deux nombres à l'utilisateur et les additionner
#Antoine Nicolleau

#Importation
import re

#Initialisation
nbuser = input("Saisir nombre 1 :  ")
nbuser2 = input ("Saisir nombre2 :  ")

#Seul les chiffres/nombres seront acceptés
nb_regex = re.compile('[1,2,3,4,5,6,7,8,9,0]')


if nb_regex.match(nbuser):
    nb_regex.match(nbuser2)
else:
    print('Entrez essentiellement des nombres !!')
    nbuser = input("Saisir nombre 1 :  ")
    nbuser2 = input ("Saisir nombre2 :  ")


total = int(nbuser) + int(nbuser2)

print(total)