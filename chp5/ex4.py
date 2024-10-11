def motdepasse():

    compteur = 0
    another = 1
    mdp = "admin123"
    
    while another == 1:
        
        saisie_mdp = input("entre le mot de passe : ")

        if not (saisie_mdp == mdp):
            compteur+=1
            print("mot de passe incorrect, accès refusé")
            another = 1
        elif saisie_mdp == mdp:
            compteur=0
            print("mot de passe correct, accès autorisé")
            another = 2

        if compteur == 3:
            print("alerte !! accès bloqué")
            break
    

  
motdepasse()