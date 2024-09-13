import random

seuil_critique = 35.0

for i in range(10):
    temperature = random.uniform(20, 40)
    if temperature > seuil_critique:
        print(f'alerte la température a dépassé le seuil critique ! : {temperature:.2f}°C')
    else:
        print(f'la température est bonne : {temperature:.2f}°C')
   
