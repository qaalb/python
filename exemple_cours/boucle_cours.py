nom = 'KORRI' # Déclaration de variable de type str
langage = 'Python' # Déclaration d'une autre variable de type str

print("\n1. #######################")
for i in range(len(nom)): # pour i dans la longueur de la chaîne
    print(nom[i], end=" ") # Affiche successivement les caractères

print("\n\n2. #######################")
for i in range(len(langage)): # pour i dans la longueur de la chaîne
    print(langage[i], end=" ") # end = " " : pour ne pas sauter de ligne
print(f"\n{len(langage)}") # Affiche la longueur de la chaîne

print("\n3. #######################")
for i in range(6): # collection de 0 à 6-1
    print(i)

print("\n4. #######################")
for i in range(5): # Collection de 0 à 5-1
    print("KORRI")

print("\n5. #######################")
for i in range(4, 8): # départ 4 à la valeur finale 8-1
    print(i)

print("\n6. #######################")
for i in range(8, 4, -1): # départ 8, finale 4+1 (-1 : décrémenter de 1)
    print(i)

print("\n7. #######################")
for i in range(0, 10, 2): # de 0 à 9 en incrémentant de 2
    print(i)

print("\n8. #######################")
for element in langage: # caractère par caractère
    print(element)
