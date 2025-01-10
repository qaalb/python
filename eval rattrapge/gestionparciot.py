from datetime import datetime

iot_devices = {
    "device1": {"mac": "00:01:32:7b:00:47", "status": "actif", "last_seen": "2025-01-01", "battery": 85},
    "device2": {"mac": "00:1B:C3:8C:00:48", "status": "inactif", "last-seen": "2024-12-20", "battery": 20},
    "device3": {"mac": "00:1C:C4:9D:99:49", "status": "actif", "last-seen": "2025-01-04", "battery": 50},
}

def ajouter_appareil(parc, device_id, mac, statut, last_seen, battery):
    if device_id not in parc:
        parc[device_id] = {"mac": mac, "status": statut, "last_seen": last_seen, "battery": battery}
        print(f"Appareil {device_id} ajouté")

def afficher_statut(parc):
    total= len(parc)
    actif = sum(1 for device in parc.values() if device["statut"] == "actif")
    inactif = total - actif
    print(f"Nombre total d'appareils : {total}")
    print(f"nombre d'appareils actif : {actif}")
    print(f"nombre d'appareil inactif: {inactif}")

def batterie_faible(parc, seuil):
    faible = [device_id for device_id, device in parc.items() if device["battery"] < seuil]
    print(f"nombre total d'appareil avec une batterie faible : {faible} ")

def mettre_a_jour_statut(parc, device_id, nouveau_statut):
    if device_id in parc:
        parc[device_id]["status"] = nouveau_statut
        print(f"le statut du {device_id} a été mis a jour")

def detecter_inactifs(parc, date_limite):
    date_limite = datetime.strptime()

def menu():
    while True:
        print("Gestion de Parc IoT")
        print("1. Afficher le statut du parc")
        print("2. Lister les appareils avec une batterie faible")
        print("3. Mettre à jour le statut d'un appareil")
        print("4. Détecter les appareils inactifs depuis trop longtemps")
        print("5. Ajouter un nouvel appareil")
        print("6. Quitter")
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            afficher_statut(iot_devices)
        elif choix == "2":
            seuil = int(input("entrez le seuil de batterie : "))
            batterie_faible(iot_devices, seuil)
        elif choix == "3":
            device_id = input("Entrez l'id du device (ex:device2) : ")
            nouveau_statut = input("Entrez le nouveau statut : ")
            mettre_a_jour_statut(iot_devices, device_id, nouveau_statut)
        elif choix == "4":
            date_limite = input("Entrez un date limite:")
            detecter_inactifs(iot_devices, date_limite)
        elif choix == "5":
            device_id = input("entrez l'id (ex:device4) : ")
            mac = input("entrez l'adresse mac (ex:00:03:55:7y:00:01) : ")
            statut = input("entrez le staut (actif/inactif) : ")
            last_seen = input("entrez la date : ")
            battery = int(input("entrez le niveau de battery : "))
            ajouter_appareil(iot_devices, device_id, mac, statut, last_seen, battery)
        elif choix == "6":
            print("Quitter")
            break
        else:
            print("choix invalide")

menu()