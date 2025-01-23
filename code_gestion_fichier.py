# # Ouvre un fichier en mode écriture

# with open("fichier.txt", "w") as file:
#     # file.write("Bonjour les bTS CIEL, ceci est une ligne de texte.")
#     file.write("Fin.")

# ############################################################
# ecriture sur plusieurs lignes

# while True:
#     ligne = input("Saisir un texte : ")

#     if ligne.lower() == 'q':
#         break  # On sort de la boucle while

#     with open("fichier.txt", "a") as fichier:
#         fichier.write(ligne + "\n")  # On ajoute un saut de ligne à chaque ligne écrite

# print("Écriture terminée.")

#############################################################
# Lecture d'un fichier


# with open("fichier.txt", "r") as file:
#     for ligne in file:
#         print(ligne.strip())
#         print(ligne.strip("\n"))
#         print(ligne)


# with open("fichier.txt", "r") as file:
#     mot_cle = "python"
#     for ligne in file:
#         if mot_cle in ligne:
#             print(ligne.strip())
#             print(ligne)
          
       

#############################################################

# Création d'un dossier

# import os
# os.mkdir("/home/ciel/mememememe")

### Vérification avec try except else


# import os

# try:
#     os.mkdir("mehdi") 
# except:
#     print("Erreur lors de la création du dossier")
# else:
#     print("Le dossier a été créé avec succès.")

#############################################################
# Vérification complexe

# import os

# try:
#     os.mkdir(":!;!:;,!:ù")
#     print("Le dossier 'unDossier' a été créé avec succès.")
# except FileExistsError:
#     print("Le dossier 'unDossier' existe déjà.")
# except OSError as e:
#     print(f"Erreur lors de la création du dossier : {e}")

#############################################################
# Récupère le répertoire courant


# import os

# chemin_actuel = os.getcwd()
# print(f"Répertoire actuel : {chemin_actuel}")



#############################################################
# # Combiner des morceaux de chemin

# import os

# chemin_actuel = os.getcwd()

# chemin = os.path.join(chemin_actuel, "Dossier", "Projets", "test.txt")
# print(f"Chemin généré : {chemin}")


#############################################################
# Création de dossier et de sous dossier

# import os

# chemin_courant = os.getcwd()
# maListe = ["python","javascript","C++"]

# for element in maListe:
#     chemin_dossier = os.path.join(chemin_courant,"dossier",element)
#     if not os.path.exists(chemin_dossier):
#         os.makedirs(chemin_dossier)
#         print("Création du dossier")
#     else:
#         print("Dossier existe déja")

#############################################################

# import os

# dossier_principal = "dossier"
# sous_dossiers = ["python","javascript","C++"]

# try:
#     os.mkdir(dossier_principal)
#     print(f"Le dossier '{dossier_principal}' a été créé avec succès.")
# except FileExistsError:
#     print(f"Le dossier '{dossier_principal}' existe déjà.")
# except OSError as e:
#     print(f"Erreur lors de la création du dossier principal : {e}")

# # Créer les sous-dossiers à l'intérieur du dossier principal
# for sous_dossier in sous_dossiers:
#     chemin_sous_dossier = os.path.join(dossier_principal, sous_dossier)
#     try:
#         os.mkdir(chemin_sous_dossier)
#         print(f"Le sous-dossier '{sous_dossier}' a été créé avec succès dans '{dossier_principal}'.")
#     except FileExistsError:
#         print(f"Le sous-dossier '{sous_dossier}' existe déjà dans '{dossier_principal}'.")
#     except OSError as e:
#         print(f"Erreur lors de la création du sous-dossier '{sous_dossier}' : {e}")


#############################################################
# Vérification avant création de dossier avec not

# import os

# if not os.path.exists("MonDossier"):
#     os.mkdir("MonDossier")
#     print("Dossier créé.")
# else:
#     print("Dossier existe déjà")


#############################################################
# Vérification avant création de fichier sans not

# import os

# if  os.path.exists("mon_fichier.txt"):
#     print("Fichier existe déjà.")
 
# else:
#     with open("mon_fichier.txt", 'w') as fichier:
#         print("Fichier créé.")
    

#############################################################
# Vérification avant création de fichier avec not

# import os

# if not os.path.exists("mon_fichier.txt"):
  
#     with open("mon_fichier.txt", 'w') as fichier:
#         pass
#     print("Fichier créé.")
# else:
#     print("Fichier existe déjà.")

#############################################################
# Vérification avant suppression de fichier

# import os

# nom_fichier = "mon_fichier.txt"
# if not os.path.exists(nom_fichier):
#     print("Le fichier n'existe pas.") 
# else:
#     os.remove(nom_fichier)
#     print("Fichier supprimé.")



#############################################################
# suppression d'un dossier vide sans vérification

# import os

# if not os.path.exists("DossierVide"):
#     os.mkdir("DossierVide")
#     print("Dossier créé.")
# else:
#     print("Dossier existe déjà")

# nom_dossier_vide = "DossierVide"

# if os.path.exists(nom_dossier_vide):
#     # Supprimer le dossier vide
#     os.rmdir(nom_dossier_vide)
#     print(f"Le dossier vide '{nom_dossier_vide}' a été supprimé.")
# else:
#     print(f"Le dossier vide '{nom_dossier_vide}' n'existe pas.")


#############################################################
# suppression d'un dossier vide avec vérification simple

# nom_dossier_vide = "DossierVide"


# if os.path.exists(nom_dossier_vide):
#     try:
#         os.rmdir(nom_dossier_vide)
#     except OSError as e:
#         print(f"Une erreur: {e} lors de la suppresion du dossier: '{nom_dossier_vide}'.")
#     else:
#         print(f"Le dossier vide '{nom_dossier_vide}' a été supprimé.")

    


#############################################################
# suppression d'un dossier non vide sans vérification 

import os
import shutil

############# CREATION D'UN DOSSIER AVEC CONTENU ############
# chemin_courant = os.getcwd()
# maListe = ["python","javascript","C++"]

# for element in maListe:
#     chemin_dossier = os.path.join(chemin_courant,"DossierAvecContenu",element)
#     if not os.path.exists(chemin_dossier):
#         os.makedirs(chemin_dossier)
#         print("Création du dossier")
#     else:
#         print("Dossier existe déja")

# Supprimer un dossier non vide
# shutil.rmtree("DossierAvecContenu")
# shutil.rmtree("DossierVide")
# print("Dossier supprimé.")



#############################################################
# suppression d'un dossier non vide avec vérification simple

# import os
# import shutil
# nom_dossier_non_vide = "MonDossier"

# if os.path.exists(nom_dossier_non_vide):
#     # Supprimer le dossier non vide
#     shutil.rmtree(nom_dossier_non_vide)
#     print(f"Le dossier non vide '{nom_dossier_non_vide}' a été supprimé.")
# else:
#     print(f"Le dossier non vide '{nom_dossier_non_vide}' n'existe pas.")



#############################################################
#  Lister le contenu d'un dossier


# import os
# #  Lister le contenu d'un dossier

# contenu = os.listdir("DossierAvecContenu")
# # contenu = os.listdir(".")  
# # contenu = os.listdir("../")
# # contenu = os.listdir("/")
# print("Contenu du répertoire courant :", contenu)




#############################################################
#  Renommer un fichier ou un dossier sans vérification.

# import os

# # Renommer un fichier
# os.rename("ancien_nom.txt", "nouveau_nom.txt")
# os.rename("DossierAvecContenu", "newDirectory")
# print("Fichier et dossier renommés.")






#############################################################
#  Vérifie si un chemin correspond à un fichier ou dossier

# import os

# chemin = "newDirectory"

# if os.path.isfile(chemin):
#     print("C'est un fichier.")
# elif os.path.isdir(chemin):
#     print("C'est un dossier.")




#############################################################
#  # Vérifier si un chemin est un fichier ou un dossier

# import os

## Vérifier si un chemin est un fichier ou un dossier
# chemin_fichier = "nouveau_nom.txt"
# chemin_dossier = "newDirectory"

# if os.path.isfile(chemin_fichier):
#     print(f"{chemin_fichier} est un fichier.")
# elif os.path.isdir(chemin_fichier):
#     print(f"{chemin_fichier} est un dossier.")
# else:
#     print(f"{chemin_fichier} n'existe pas.")

# if os.path.isfile(chemin_dossier):
#     print(f"{chemin_dossier} est un fichier.")
# elif os.path.isdir(chemin_dossier):
#     print(f"{chemin_dossier} est un dossier.")
# else:
#     print(f"{chemin_dossier} n'existe pas.")


#############################################################
#  Copier, déplacer ou renommer un fichier

# import shutil

# # Copier un fichier
# shutil.copy("source.txt", "destination.txt")

# # Déplacer un fichier
# shutil.move("source.txt", "newDirectory/source.txt")


#############################################################
#  Trouve des fichiers ou des dossiers selon un modèle (wildcards).

# import glob

# # Trouver tous les fichiers .txt
# fichiers = glob.glob("*.txt")
# print("Fichiers trouvés :", fichiers)


#############################################################
# Fournit des informations détaillées sur un fichier ou un dossier (taille, permissions, etc.).

# import os

# # Obtenir des informations sur un fichier
# info = os.stat("meteo_commune.py")
# # print(f"Taille : {info.st_size} octets")
# print(f"Taille : {info} octets")


#############################################################
# Extraction de l'extension

# import os

# chemin = "document.txt"
# base, extension = os.path.splitext(chemin)
# print(f"Base : {base}, Extension : {extension}")

# #Résultat:  Base : document, Extension : .txt

# # Exemple 2
# chemin = "/chemin/vers/fichier.tar.gz"
# base, extension = os.path.splitext(chemin)
# print(f"Base : {base}, Extension : {extension}")

# # Exemple 3
# chemin = "mon_fichier"
# base, extension = os.path.splitext(chemin)
# print(f"Base : {base}, Extension : {extension}")

# # Exemple 4
# chemin = "archive.tar.gz.bz2"
# base, extension = os.path.splitext(chemin)
# print(f"Base : {base}, Extension : {extension}")




#############################################################
# Affichage des infos sur le fichier


# import os

# # Parcourir un dossier
# for chemin, dossiers, fichiers in os.walk("warmup"):
#     print(f"Chemin : {chemin}")
#     print(f"Dossiers : {dossiers}")
#     print(f"Fichiers : {fichiers}")



# Traitement de fichiers volumineux 
# with open("large_file.txt", "r") as file:
#     chunk = file.read(1024)



# Mode binaire
# with open("image.png", "rb") as file:
#     data = file.read()


# Permissions restrictives :

# os.chmod("secure_file.txt", 0o600)


# with open("example.txt", "r") as file:
#     lines = file.readlines()

# print(lines)

