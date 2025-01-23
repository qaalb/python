def est_longueur_valide(mot_de_passe):
    return len(mot_de_passe) >= 8

def contient_caractere_special(mot_de_passe):
    special_caracteres = "@#$%&"
    for caracter in mot_de_passe:
        if caracter in special_caracteres:
            return True
    return False

def contient_majuscule_et_minuscule(mot_de_passe):
    return (i.lower() for i in mot_de_passe) and (i.upper() for i in mot_de_passe)

def contient_chiffre(mot_de_passe):

    for caracter in mot_de_passe:
        if caracter.isdigit():
            return True
    return False

def verifier_mot_de_passe():
    mot_de_passe = input("Veuillez saisir un mot de passe : ")
    
    criteres_non_respectes = []
    
    if not est_longueur_valide(mot_de_passe):
        criteres_non_respectes.append("Longueur minimale de 8 caractères")
    
    if not contient_caractere_special(mot_de_passe):
        criteres_non_respectes.append("Doit contenir au moins un caractère spécial (@, #, $, %, &)")
    
    if not contient_majuscule_et_minuscule(mot_de_passe):
        criteres_non_respectes.append("Doit contenir au moins une majuscule et une minuscule")
    
    if not contient_chiffre(mot_de_passe):
        criteres_non_respectes.append("Doit contenir au moins un chiffre")

    if not criteres_non_respectes:
        print("Mot de passe valide.")
    else:
        print("Mot de passe invalide. Les critères non respectés sont :")
        for critere in criteres_non_respectes:
            print(f"{critere}")

verifier_mot_de_passe()

