#!/usr/bin/python3
#1b-dic.py
#Lister les noms entrer par les utilisateur par ordre alphabétique
#Antoine Nicolleau

#Importation
import re

#Initialisation
str_regex = r"[a-zA-Z][&~#{'{[(|`_^@)°=+}><]"
nameList = []
userInput=""

# appuyer sur q pour quitter + saisie utilisateur et ajout à la liste
while userInput != 'q':
    userInput = input('Veuillez saisir un prénom. Entrez q pour quitter : ')
    if userInput != 'q':
        if re.match(str_regex, userInput) is not None:
            nameList.append(userInput)
        
        else: 
            print('Votre nom comporte des éléments invalides. veuillez réessayer.')


#.sort pour trier les noms dans la liste.
nameList.sort()
print(nameList)