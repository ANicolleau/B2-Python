#!/usr/bin/python3
#3c-ssh.py
#archive et sauvegarde d'un dossier
#Antoine Nicolleau

#Importation
import shutil
import os.path
import gzip
import sys
import signal
import argparse
from paramiko import SSHClient
from scp import SCPClient


#Fonction
def leaver (sig, frame):
    print('vous avez interrompu le programme')
    sys.exit(0)


# Interception du Ctrl+c
signal.signal(signal.SIGINT, leaver)


#Lancement du script avec option.
opt_lancement = argparse.ArgumentParser(description='archive et sauvegarde d\'un dossier possible en ssh si précision d\'une adresse IP')
opt_lancement.add_argument('orig_folder', type=str, help='Répertoire d\'origine')
opt_lancement.add_argument('new_folder', type=str, help='Répertoire de destination, si une IP est entré, ce fichier sera envoyé en ssh')
opt_lancement.add_argument('username', type=str, help='identifiant pour authentification')
opt_lancement.add_argument('password', type=str, help='mot de passe')
opt_lancement.add_argument('ipaddr', type=str, help='Adresse IP')

option = opt_lancement.parse_args()

#Initialisation
orig_folder = os.path.expanduser(option.orig_folder)
new_folder = os.path.expanduser(option.new_folder) + '.tar.gz'
arch_file = orig_folder + '.tar.gz'


#Connection ssh
if (option.username != None and option.password != None):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(option.ipaddr, username = option.username, password = option.password)

    scp = SCPClient(ssh.get_transport())
    
    if (os.path.exists(orig_folder) == False):
        sys.stderr.write('Le dossier 3btest n\'éxiste pas' + '\n')

    else:
        shutil.make_archive(orig_folder,'gztar','.',orig_folder)
    
        #On enregistre le contenu des fichiers dans des variables pour pouvoir les comparés
        if(os.path.exists(new_folder) == True):
            with gzip.open(arch_file) as fichier:
                new_file = fichier.read()

            with gzip.open(new_folder) as fichier:
                old_file = fichier.read()

            if (old_file != new_file):
                shutil.move(os.path.join('', arch_file), os.path.join('data/', arch_file))
                sys.stdout.write('remplacer' + '\n')
                scp.put(arch_file)
            else : 
                sys.stdout.write('pas remplacer' + '\n')
                os.remove(arch_file)

        else : 
            sys.stdout.write("Rien dans le dossier je déplace ce fichier" + '\n')
            shutil.move(arch_file,new_folder)
            scp.put(arch_file)

elif(option.username != None):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(option.ipaddr, username = option.username)

    scp = SCPClient(ssh.get_transport())
    
    if (os.path.exists(orig_folder) == False):
        sys.stderr.write('Le dossier 3btest n\'éxiste pas' + '\n')

    else:
        shutil.make_archive(orig_folder,'gztar','.',orig_folder)
    
        #On enregistre le contenu des fichiers dans des variables pour pouvoir les comparés
        if(os.path.exists(new_folder) == True):
            with gzip.open(arch_file) as fichier:
                new_file = fichier.read()

            with gzip.open(new_folder) as fichier:
                old_file = fichier.read()

            if (old_file != new_file):
                shutil.move(os.path.join('', arch_file), os.path.join('data/', arch_file))
                sys.stdout.write('remplacer' + '\n')
                scp.put(arch_file)
            else : 
                sys.stdout.write('pas remplacer' + '\n')
                os.remove(arch_file)

        else : 
            sys.stdout.write("Rien dans le dossier je déplace ce fichier" + '\n')
            shutil.move(arch_file,new_folder)
            scp.put(arch_file)

else:
    #Si le fichier n'éxiste pas, affiche ça dans la console, sinon continue.
    if (os.path.exists(orig_folder) == False):
        sys.stderr.write('Le dossier 3btest n\'éxiste pas' + '\n')

    else:
        shutil.make_archive(orig_folder,'gztar','.',orig_folder)
            
        #On enregistre le contenu des fichiers dans des variables pour pouvoir les comparés
        if(os.path.exists(new_folder) == True):
            with gzip.open(arch_file) as fichier:
                new_file = fichier.read()

            with gzip.open(new_folder) as fichier:
                old_file = fichier.read()

            if (old_file != new_file):
                shutil.move(os.path.join('', arch_file), os.path.join('data/', arch_file))
                sys.stdout.write('remplacer' + '\n')
            else : 
                sys.stdout.write('pas remplacer' + '\n')
                os.remove(arch_file)

        else : 
            sys.stdout.write("Rien dans le dossier je déplace ce fichier" + '\n')
            shutil.move(arch_file,new_folder)