mdp= input("creer votre mot de passe : ")
tentatives = 3

for tentative in range(tentatives):
    mdpsaisi = input("entrez votre mot de passe : ")
    if mdpsaisi == mdp:
     print("connexion réussie !")
     break   
    else:
        tentatives_restantes = tentatives - (tentative + 1)
        if tentatives_restantes > 0:
            print(f"mot de passe incorrect il reste {tentatives_restantes} tentative.")
        else:
            print("connexion echouée")   
