def saisir():

    nb = 0 
    while nb == 0:
        nb_saisir = input("saisissez un nombre entier positif : ")
        try:
            nb = int(nb_saisir)
        except:
            print("vous n'avez pas saisi une valeur numérique")
            nb_saisir = input("Veuillez saisir un nombre entier positif : ")
        else:
            if nb == 0:
                print("vous avez saisi une valeur égale à zéro")
                nb_saisir = input("Veuillez saisir un nombre entier positif : ")
            elif nb < 0:
                print("vous avez saisi une valeur inférieure à zéro")
                nb_saisir = input("Veuillez saisir un nombre entier positif : ")
            elif nb > 0:
                print("votre valeur est correcte")
                return nb
