from random import randint

essai = 0

while True:
    nb1, nb2 = randint(1, 20), randint(1, 20)
    while True:
        try:
            somme = int(input(f"quelle est la somme de {nb1} + {nb2} ? "))
            break 
        except:
            print("vous n'avez pas saisi une valeur numérique valide essayez encore")

    if somme == nb1 + nb2:
        print("bravo vous avez trouvé la bonne réponse !")
        break
    else:
        essai += 1
        print(f"mauvaise réponse. nombre d'essais : {essai}")
