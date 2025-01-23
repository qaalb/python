class Ordinateur:
    def __init__(self, att_marque, att_prix) :
        self.marque = att_marque
        self.prix = att_prix

    def afficher(self):
        print(self.marque)
        print(f"{self.prix} euro")

    def afficher_return(self):
        return self.marque, self.prix

monOrdinateur = Ordinateur("HP Prodesk", "699.55")
monOrdinateur.afficher()

marque, prix = monOrdinateur.afficher_return()
print(f"Le PC {marque} coute {prix} €")

class CapteurMeteo:
    def __init__(self, nom, emplacement, date_installation) :
        self.nom = nom
        self.emplacement = emplacement
        self.date_installation = date_installation
        print("TEST")

    def afficher_infos(self):
        print(self.nom)
        print(self.emplacement)
        print(self.date_installation)
    
Capteur1 = CapteurMeteo("Capteur TEMPERATURE", "PARIS", "12/12/2012")
Capteur2 = CapteurMeteo("Capteur HUMIDITE", "CLICHY", "15/08/2024")
Capteur3 = CapteurMeteo("Capteur PH", "PANTIN", "21/09/2025")


Capteur1, Capteur2, Capteur3 = CapteurMeteo.afficher_infos()








# class Personne:
#     def __init__(self) :
#         # print("Le constructeur est lancé")
#         pass


# unePersonne = Personne()
# print(unePersonne)


# #################
#######################################

# class point():
#     """un 
#     jolie
#             commentaire"""


# p = point()
# p.x = 3.0
# p.y = 12
# print(p.__doc__)
# print(p.x)
# print(p.y)

# ########################################################


# class Personne:
#     def __init__(self,nom,prenom,residence,age):
#         self.nom = nom
#         self.prenom = prenom
#         self.residence= residence
#         self.age = age

# unePersonne = Personne("KORRI","Ilyas","Clichy",47)

# print(unePersonne.nom,unePersonne.prenom,unePersonne.residence,unePersonne.age)



# ########################################################

# class Personne:
#     def __init__(self, att_prenom , att_nom= "KORRI") :
#         self.nom = att_nom
#         self.prenom = att_prenom
#         print("Le constructeur est lancé")

# unePersonne = Personne("Samuel","BOUHENIC")
# moi = Personne("ilyas")
# print(unePersonne.prenom)
# print(moi.nom)
# print(moi.prenom)
# print(unePersonne.nom)


# ########################################################


# class Personne:
#     def __init__(self, att_nom= "KORRI" , att_prenom= "Ilyas") :
#         self.nom = att_nom
#         self.prenom = att_prenom
#         print("Le constructeur est lancé")


#     def afficher(self):
#         print("#"*20)
#         print(self.prenom)
#         print(self.nom)
#         print("*"*20)


# moi = Personne()
# unePersonne = Personne("DJENDLI","Sara")

# unePersonne.afficher()
# moi.afficher()


# ########################################################


# class Personne:
#     def __init__(self, att_nom , att_prenom, note1, note2, note3 ) :
#         self.nom = att_nom
#         self.prenom = att_prenom
#         self.note1 = note1
#         self.note2 = note2
#         self.note3 = note3
#         print("Le constructeur est lancé")


#     def afficher(self):
#         print(self.prenom)
#         print(self.nom)
#         self.moyenne = (self.note1 +self.note2 +self.note3)/3
#         return self.moyenne


# unePersonne = Personne("DIAH","Samy",8,9,19)

# moyenne = unePersonne.afficher()
# print(f"La moyenne de {unePersonne.prenom} est : {unePersonne.moyenne}")

# ########################################################

# class Personne:
#     def __init__(self, att_nom , att_prenom ) :
#         self.nom = att_nom
#         self.prenom = att_prenom
#         print("Le constructeur est lancé")

  
  
#     def afficher(self):
#         print(self.prenom)
#         print(self.nom)
       
# unePersonne = Personne("KORRI","Ilyas")

# # moyenne = unePersonne.afficher()
# print(unePersonne.__dict__)



# ########################################################



# class Ordinateur :
#     def __init__(self,att_marque, att_prix) :
#         self.marque = att_marque
#         self.prix = att_prix
#         print("Appel constructeur")


#     def afficher_sans_retour(self):
#         print(self.marque)
#         print(f"{self.prix} euro")
     
    
#     def afficher_avec_retour(self):
#         return self.marque, self.prix


# monOrdinateur = Ordinateur("Macbook", "17")
# monOrdinateur.afficher_sans_retour()
# marque, prix= monOrdinateur.afficher_avec_retour()
# print(f"L'ordinateur de marque {marque} coute: {prix} €")

# unPC = Ordinateur("LG",2000)
# unAutrePC = Ordinateur("Acer",3000)

# unPC.afficher()

# print("______")

# unAutrePC.afficher()

   
# ########################################################


# class Personne():
#     def __init__(self,nom,codeur) -> None:
#         self.nom = nom
#         self.codeur= codeur

#     def isCoder(self):
#         if self.codeur:
#             print("Est codeur")
#         else:
#             print("N'est pas codeur")

#     def __str__(self) -> str:
#         return f"nom: {self.nom},\ncodeur: {self.codeur}"


# ilyas= Personne("KORRI",True)
# print(ilyas)
# ilyas.isCoder()
    
# ########################################################

# class Personne:
#     def __init__(self, att_nom= "KORRI" , att_prenom= "Ilyas") :
#         self.nom = att_nom
#         self.prenom = att_prenom
#         print("Le constructeur est lancé")


#     def afficher(self):
#         print("#"*20)
#         print(self.prenom)
#         print(self.nom)
#         print("#"*20)


# moi = Personne()
# unePersonne = Personne("DJENDLI","Sara")

# unePersonne.afficher()
# moi.afficher()