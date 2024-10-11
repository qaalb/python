packets = [
(500, 'TCP'),
(1000, 'UDP'),
(2000, 'TCP'),
(50, 'ICMP'),
(1600, 'TCP'),
(800, 'UDP')
]

# print(packets[1])
nb = 0
nb_1 = 0

for element in packets:
    if element[0] >= 1500:
        
        print(f"Paquets qui dépassent 1500 octets : \n{element}")
        

for element2 in packets:
    if element2[1] == 'UDP':
        nb+=1


for element3 in packets:
    if element3[1] == 'TCP':
        nb_1+=1
        
        
print(f"\nNous comptons {nb_1} paquets contenant du TCP")
calcul_tcp = nb_1/len(packets)*100
print(f"Pourcentage de paquets UDP : {calcul_tcp:.2f}%\n")


print(f"Nous comptons {nb} paquets contenant de l'UDP")
calcul_udp = nb/len(packets)*100
print(f"Pourcentage de paquets UDP : {calcul_udp:.2f}%")