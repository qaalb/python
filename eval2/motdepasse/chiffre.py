def contient_chiffre(mot_de_passe):
    for caractere in mot_de_passe:
        if caractere.isdigit():
            return True
    return False