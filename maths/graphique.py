
# import matplotlib.pyplot as plt

# heures = [1, 2, 3, 4, 5]
# trafic = [120, 200, 150, 300, 250]

# plt.plot(heures, trafic)
# plt.title("Trafic réseau (en paquets)")
# plt.xlabel("Heures")
# plt.ylabel("Nombre de paquets")
# plt.grid(True)
# plt.show()


# ####################################################################

# # histogramme ##

# import matplotlib.pyplot as plt

# tailles = [60, 60, 80, 90, 100, 90, 90, 130, 140, 150]

# plt.hist(tailles, bins=5, color='skyblue', edgecolor='black')
# plt.title("Répartition des tailles de paquets")
# plt.xlabel("Taille (octets)")
# plt.ylabel("Fréquence")
# plt.show()

# ####################################################################

# import matplotlib.pyplot as plt
# import numpy as np

# # Simuler des données de temps de réponse (en ms)
# response_times = np.random.normal(loc=50, scale=10, size=1000)

# # Graphique
# plt.hist(response_times, bins=20, color='blue', alpha=0.7)
# plt.title("Distribution des temps de réponse")
# plt.xlabel("Temps (ms)")
# plt.ylabel("Fréquence")

# plt.show()


# ####################################################################

# import matplotlib.pyplot as plt

# dispositifs = ['CaptA','CaptB','R1','Cam']
# utilisation_cpu = [20, 35, 50, 65]

# plt.bar(dispositifs, utilisation_cpu, color='green')
# plt.title("Utilisation CPU par dispositif IoT")
# plt.xlabel("Dispositifs")
# plt.ylabel("Utilisation CPU (%)")
# plt.show()

# ####################################################################


# import matplotlib.pyplot as plt

# protocoles = ['HTTP', 'HTTPS', 'FTP', 'SSH']
# parts = [40, 35, 15, 10]

# plt.pie(parts, labels=protocoles, 
#         autopct='%1.1f%%')
# plt.title("Répartition des protocoles réseau")
# plt.show()


####################################################################


## Exercice 1 ##

# import matplotlib.pyplot as plt

# ip_addresses = ["192.168.1.1", "10.0.0.2", "172.16.0.5", "192.168.1.1",
# "10.0.0.2", "10.0.0.2"]

# dispositifs = (ip_addresses)
# freq = [0, 0.5, 1, 1.5, 2, 2.5, 3]

# plt.title("Fréquence des adresses IP suspectes")
# plt.show()


import matplotlib.pyplot as plt

ip_addresses = ["192.168.1.1", "10.0.0.2", "172.16.0.5", "192.168.1.1",
"10.0.0.2", "10.0.0.2"]

freq = [0.5, 1, 1.5, 2, 2.5, 3]

plt.bar(ip_addresses, freq, color=['blue', 'yellow', 'green'])
plt.title("Fréquence des adresses IP suspectes")
plt.xlabel("Adresses IP")
plt.ylabel("Fréquence")
plt.show()


ip_addresses.count



