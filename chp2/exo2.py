from random import randint

while True:
    nb1, nb2 = randint(1, 100), randint(1, 100)
    somme = int(input(f"quelle est la somme de {nb1} + {nb2} ? " ))
    
    if somme == nb1 + nb2:
        print("bravo vous avez trouvé la bonne réponse")
        break
    else:
        print("mauvaise réponse reessayer")
        
