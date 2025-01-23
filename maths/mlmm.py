reseau = {
    1: {"source": "192.168.0.1", "destination": "192.168.0.2", "type": "IPv4", "etat": "transmise"},
    2: {"source": "192.168.0.3", "destination": "192.168.0.4", "type": "ARP", "etat": "perdue"},
    3: {"source": "192.168.0.5", "destination": "192.168.0.6", "type": "IPv4", "etat": "transmise"},
}

def ajouter_trame(id, source, destination, type, etat, reseau):
      reseau = {"id" : id, "source" : source, "destination" : destination, "type" : type, "etat" : etat}
      if id in reseau:
        print("Erreur cet ID existe déjà")
      else:
        reseau[id]=source, destination, type, etat
      else:
      print("Aurevoir")
      break


def modifier_etat_trame(id, nouvel_etat, reseau):
    reseau = {"id" : id, "nouvel_etat" : "etat"}
    if id not in reseau:
        print(f"Cet ID {id} n'a pas été trouvé")



modifier_etat_trame(2,"transmie",reseau)
print(reseau)



def supprimer_trame(id, reseau):
    if id not in reseau:
        print(f"Cet ID {id} n'a pas été trouvé")
        break
    else:
    # del reseau["id=2"]
        id("5").clear()
        print(reseau)
else:
    print("Aucune donnée enregistrée")



def afficher_trames_par_type(type, reseau):
    print("Affichage des trames ayant un type ARP:")
    for type("ARP"), source, destination, etat in reseau.items():
        print(f"Type : {type}")
        print(f"Adresse Source : {source}")
        print(f"Adresse Destination : {destination}")
        print(f"Etat : {etat}")

def calculer_statistiques(reseau):
    print(len(reseau))
    reseau_perdue = sum(1 for etat in reseau.values() if etat == "perdue")
    print(reseau_perdue)