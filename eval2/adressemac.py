# continuer = True

# while continuer:
#     mac = input("Saisir l'adresse MAC: ")
#     valide = True
#     if mac.count(":") == 5:
#         octets = mac.split(":")
#         for octet in octets:
#             if len(octet) != 2:
#                 print("Chaque octet doit contenir 2 caractères")
#                 valide = False
#                 break
#             for caractere in octet:
#                 if caractere.lower() not in "abcdef0123456789":
#                     print(f"{caractere} n'est pas un caractère hexadécimal valide")
#                     valide = False
#                     break
#             if not valide:
#                 break
#     else:
#         print("Le nombre d'octets est incorrect")
#         valide = False

#     if valide:
#         print(f"{mac} est valide")
#         continuer = False
#     else:
#         print("Adresse MAC invalide, veuillez réessayer.")




def est_groupe_hex_valide(groupe):
        if len(groupe)!=2:
             return False
        for caractere in groupe:
                if caractere.lower() not in "abcdef0123456789":
                    print(f"{caractere} n'est pas un caractère hexadécimal valide")
                    valide = False
                    break
                if not valide:
                    break


def est_mac_valide(mac):
       if mac.count(":") == 5:
        return True
       elif mac.count("-") == 5:
        return True
       else:
        return False      


def saisir_mac():
     while True :
         mac = input("Saisir l'adresse MAC: ")

         if est_mac_valide(mac):
            print("Adresse MAC valide")
            break
         else:
            print("Adresse MAC invalide. Veuillez réessayer.")

saisir_mac()
