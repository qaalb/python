from random import uniform
import random

def bd_passante(seuil_bande_passante):

    nb=15
    echec=0
    iteration = 0
    for i in range(nb):
        iteration+=1
        debit_reseau = random.uniform(50, 110)
       
        if debit_reseau > seuil_bande_passante:
            print(f"Itération {iteration}: Débit réseau {debit_reseau:.2f} Mbps dépasse le seuil de {seuil_bande_passante} Mbps.")
            echec+=1
            
        else:
            print(f"Itération {iteration}: Débit réseau {debit_reseau:.2f} Mbps est sous contrôle.")
            echec=0

        if echec == 3:
            print("Vous devez couper la connexion internet, le seuil a été dépassé 3 fois de suite")
            break
            

seuil_critique = 100
bd_passante(seuil_critique)