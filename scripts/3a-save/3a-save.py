#!/usr/bin/python3
#3a-save.py
#archive et sauvegarde d'un dossier
#Antoine Nicolleau

#Importation
import shutil
import os.path
import gzip
import sys
import signal


#Fonction
def leaver (sig, frame):
    print('vous avez interrompu le programme')
    sys.exit(0)

# Interception du Ctrl+c
signal.signal(signal.SIGINT, leaver)

#Initialistation
orig_file = '3atest'
arch_file = '3atest.tar.gz'
dest_file = 'data/3atest.tar.gz'


#Si le dossier n'éxiste pas, affiche ça dans la console, sinon continue.
if (os.path.exists(orig_file) == False):
    sys.stderr.write('Le dossier 3atest n\'éxiste pas' + '\n')

else:
    shutil.make_archive(orig_file,'gztar','.',orig_file)
    
    #On enregistre le contenu des dossier dans des variables pour pouvoir les comparés
    if(os.path.isfile(dest_file) == True):
        with gzip.open(arch_file) as fichier:
            new_file = fichier.read()

        with gzip.open(dest_file) as fichier:
            old_file = fichier.read()

        if (old_file != new_file):
            shutil.move(os.path.join('', arch_file), os.path.join('data/', arch_file))
            sys.stdout.write('remplacer' + '\n')
        else : 
            sys.stdout.write('pas remplacer' + '\n')
            os.remove(arch_file)

    else : 
        sys.stdout.write("Rien dans le dossier je déplace ce fichier" + '\n')
        shutil.move(arch_file,dest_file)
        




    


