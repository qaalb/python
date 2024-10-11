def mesure():
    taille = 0
    poids = 0

    while taille == 0 or poids == 0:

        mesure_poids = input("quelle est ton poids en kg ? : ")
        mesure_taille = input("quelle est ta taille en cm ? : ")

        try:
            poids = int(mesure_poids)
            taille = int(mesure_taille)
        except:
            print("vous n'avez pas saisi une valeur numérique")
        else:
            if taille == 0 or poids == 0:
                print("vous avez saisi une valeur égale à zéro")
            elif taille < 0 or poids < 0:
                print("vous avez saisi une valeur inférieure à zéro")
                taille = 0
                poids = 0
            elif taille > 0 or poids > 0:
                print("vos valeurs sont correctes")
                return poids, taille
    