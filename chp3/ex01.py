# Utilisateur correct prédéfini
utilisateur_correct = "admin"
# Nombre maximum de tentatives
max_tentatives = 3
# Compteur de tentatives
tentatives = 0

while tentatives < max_tentatives:
    utilisateur = input("entrez le nom d'utilisateur : ")
    if utilisateur == utilisateur_correct:
        print("connexion réussi !")
        break
    else:
        tentatives += 1
        print(f"échec de la connexion. tentatives restantes : {max_tentatives - tentatives}")

if tentatives == max_tentatives:
    print("nombre maximum de tentatives atteint accès refusé")
