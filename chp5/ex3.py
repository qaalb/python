import random

def nb_connex(nb_tentativ):

    log=["réussie","échec"]

    nb_echec = 0
    
    iteration=0
    for i in range(10):
        iteration+=1
        for paquet in log:
            paquet = random.choice(log)
        print(f"Tentative {iteration}: Connexion {paquet}")

        if paquet == "réussie":
            nb_echec=0
        elif paquet == "échec":
            nb_echec+=1

        if nb_echec == 3:
            print(f"{nb_echec} connexions échouées consécutives. Compte bloqué.")
            break
        
            

nb_connex(10)