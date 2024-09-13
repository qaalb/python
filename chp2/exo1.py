#moyenne = input("Quel est votre moyenne? : ")

#Gestion des erreurs
moyenne_int = "rien"

while moyenne_int == "rien":
    moyenne_str = input("Quelle est votre moyenne? : ")
    try:
        moyenne_int = int(moyenne_str) # si le cast fonctionne je passe à la suite :(else) et je saute except

    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")

    else:
        if moyenne_int < 0: # si la valeur saisie est négative
            print("la note doit être comprise entre 0 et 20.")
            moyenne_int = "rien"  #je réaffecte 0 à moyenne_int pour revenir à la condition initiale

        elif moyenne_int > 20:
            print("la note doit être comprise entre 0 et 20.")
            moyenne_int = "rien"

        elif moyenne_int >= 18:
            print("Excellent")

        elif 14 <= moyenne_int < 18:
            print("Très bien")

        elif 10 <= moyenne_int < 14:
            print("Assez bien")

        elif 5 <= moyenne_int < 10:
            print("Insuffisant")

        elif 0 <= moyenne_int < 5:
            print("Catastrophique")

        else:
            print("Erreur")