#Exercice 1 

class EquipementReseau:
    def __init__(self, nom, adresse_ip):
        self.nom = nom
        self.adresse_ip = adresse_ip

    def afficher_info(self):
        print(self.nom)
        print(self.adresse_ip)

class ConnexionReseau:
    def __init__(self, equipement1: EquipementReseau, equipement2: EquipementReseau, type_connexion: str):
        self.equipement1 = equipement1
        self.equipement2 = equipement2
        self.type_connexion = type_connexion
        pass
    def afficher_details(self):
        print("Détails de la connexion :")
        self.equipement1.afficher_info()
        self.equipement2.afficher_info()
        print(f"Type de connexion : {self.type_connexion}")

        # Création des équipements réseau
equipement1 = EquipementReseau("Switch01", "192.168.1.1")
equipement2 = EquipementReseau("Router01", "192.168.1.254")
# Création d'une connexion réseau
connexion = ConnexionReseau(equipement1, equipement2, "Ethernet")
# Affichage des détails de la connexion
connexion.afficher_details()

#Exercice 2 

class PeripheriqueIoT:
    def __init__(self, nom, adresse_mac, statut="Inactif"):
        self.nom = nom
        self.adresse_mac = adresse_mac
        self.statut = statut
    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut









class GestionIoT:
    def __init__(self):
        self.peripheriques = 
