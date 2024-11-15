
def est_segment_valide(segment):

        if segment.isdigit() : 
            if 0 <= int(segment) <= 255:
                return True
            else:
                return False  
        else:
            return False

def est_ip_valide(ip):
    valide = False

    octets = ip.split('.')
    if len(octets) == 4:
        for octet in octets:
            if not est_segment_valide(octet):
                valide = False
                break
            else:
                valide = True
    else:
        valide = False
    return valide

def saisir_ip():
     while True: 
        ip = input("Entrez une adresse IP : ")
        if est_ip_valide(ip):
            print("Adresse IP valide")
            break 
        else:
            print("Adresse IP invalide")

saisir_ip()