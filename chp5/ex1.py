def trame(latitude, longitude):
    appareil = 0
    if not(-90 <= latitude   <= 90 and -180 <=longitude <= 180):
        appareil += 1
        print(f"{appareil} appareil doit être marqué pour vérification")

    else:
        print("les coordonnées sont correctes")

latitude = int(input("entrez une valeur correspondant à latitude : "))
longitude = int(input("entrez une valeur correspondant à longitude : "))

trame(latitude, longitude)