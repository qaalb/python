#age = input("Quel est votre age? : ")

#Gestion des erreurs
continuer = 0
while continuer == 0:
    note_str = input("Quelle est votre moyenne ? : ")
    try:
        note_int = int(note_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")

    else:
        if note_int < 0: # si la valeur saisie est = zéro
            print("Vous avez < zéro")
            continuer = 0

        elif note_int > 20: # si la valeur saisie est négative
            print("Vous avez saisi une valeur > 20")
            continuer = 0  #je réaffecte 0 à note_int pour revenir à la condition initiale

        elif note_int >= 18:
            print("Excellent")
            continuer = 1

        elif 14 <= note_int < 18:
            print("Très bien")
            continuer = 1

        elif 10 <= note_int < 14:
            print("Assez bien")
            continuer = 1

        elif 5 <= note_int < 10:
            print("Insuffisant")
            continuer = 1

        elif 0 <= note_int < 5:
            print("Catastrophique")
            continuer = 1

        else:
            print("Erreur")