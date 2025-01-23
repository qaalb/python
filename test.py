import os

try:
    os.mkdir("mehdi") 
except:
    print("Erreur lors de la création du dossier")
else:
    print("Le dossier a été créé avec succès.")