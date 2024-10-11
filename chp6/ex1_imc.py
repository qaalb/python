def mesureIMC(poids, taille):
    
    taille_m = taille / 100  
    imc = poids / (taille_m ** 2)
    
    print(f"votre imc est de {imc:.2f}")
    if imc < 18.5:
        print("vous êtes maigre")
    elif imc >= 18.5 and imc < 25:
        print("vous êtes normal")
    elif imc >= 25 and imc < 30:
        print("vous êtes en surpoids")
    elif imc >= 30 and imc <= 40:
        print("vous êtes en obesité modérée")
    elif imc > 40:
        print("vous êtes en obesité morbide")
    return imc