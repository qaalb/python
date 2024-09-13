try:
    moyenne = int(input("Saisir votre note : "))

    if moyenne < 0 or moyenne > 20:
        print("la note doit être comprise entre 0 et 20.")
    else:
        if moyenne >= 18:
            print("Excellent")
        elif 14 <= moyenne < 18:
            print("Très bien")
        elif 10 <= moyenne < 14:
            print("Assez bien")
        elif 5 <= moyenne < 10:
            print("Insuffisant")
        else:
            print("Catastrophique")

except ValueError:
    print("veuillez entrer un nombre entier.")
