def contient_caractere_special(mot_de_passe):
    for caractere in mot_de_passe:
        if caractere not in "@#$%&":
            print("Mot de passe invalide. Veuillez saisir au moins un caractère spécial comme (@, #, $, %, &)")
            return False
        else:        
            return True
        