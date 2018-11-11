#!/usr/bin/python3
#1c-moy.py
#Demander une saisie utilisateur de plusieurs notes et prénoms
#Antoine Nicolleau

#initialisation
my_dict = {}
name_input = input('Saisir un prénom :   ')
nb_input = 0


while(str(name_input) is str):
    print('On est dans le 1e while')
    name_input = input('Veuillez saisir un prénom et non autre chose :   ')

while(str(nb_input) is str):
    print('On est dans le 2e while')
    nb_input = int(input('Saisir une note pour l\'élève que vous venez de rentrer, ne pas saisir de lettre :   '))
    if int(nb_input) < 0 or int(nb_input) > 20:
        nb_input = input('Une note se situe entre 0 et 20, elle est essentiellement composée de chiffre. Réessayer:   ')


my_dict = {str(name_input) : int(nb_input)}

while (str(name_input) != 'q' ):
    print('On est dans le 3e while')
    name_input = input('Saisir un prénom :   ')
    if str(name_input) == 'q':
        print(my_dict)
        exit(0)

    else:
        nb_input = input('Saisir une note pour l\'élève que vous venez de rentrer :   ')
        
        if int(nb_input) < 0 or int(nb_input) > 20:
            nb_input = input('Une note se situe entre 0 et 20, elle est essentiellement composée de chiffre. Réessayer:   ')
        
        elif(str(name_input) is not int or int(nb_input) is not str ):
            my_dict[str(name_input)] = int(nb_input)
        
        elif (str(name_input) is not str or str(nb_input) is not int) :
            print("Ceci n'est pas un nombre, veuillez réessayer")

print(my_dict)