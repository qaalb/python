import os
import glob

# if os.path.exists("mesDossier"):
#     return
# else:
#     print("le dossier n'existe pas")

# def identifier(repertoire):
#     contenu = os.listdir(repertoire)
#     fichier_txt = glob.glob(".txt")
#     # print(contenu)
#     if fichier_txt:
#         print(f"Fichiers.txt dans le répertoire {repertoire} :")
#         print("/n"(fichier_txt))
#     else:
#         print(f"Aucun Fichiers.txt dans le répertoire : {repertoire}")
#         # except Exception 

# identifier("mesDossiers")


def lister_contenu(chemin_dossier):
    contenu = os.listdir(chemin_dossier)
    for element in contenu:
        chemin_complet = os.path.join(chemin_dossier, element)
        if os.path.isdir(chemin_complet):
            lister_contenu(chemin_complet)
        elif element.endswith('.txt'):
            print(f"Fichier.txt dans le répertoire : {os.path.basename (chemin_complet)}")

lister_contenu("mesDossier")