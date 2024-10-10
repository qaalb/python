ip = input("Saisir l'adresse IP Source : ")
octets = ip.split('.')

if len(octets) != 4:
    print("Adresse IP source invalide, veuillez réessayer.")
else:
    valide = True