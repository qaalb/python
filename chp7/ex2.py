logs = [
('192.168.1.1', '2024-09-12 12:15:10'),
('192.168.1.2', '2024-09-12 12:16:15'),
('192.168.1.1', '2024-09-12 12:20:20'),
('192.168.1.3', '2024-09-12 12:30:25'),
('192.168.1.1', '2024-09-12 12:35:30')
]

tab = []

# print(logs[2])

for element in logs:
    # print(tab)
    if element not in tab:
        tab.append(element[0])
    
print(tab)

for element2 in tab:
    nb = tab.count(element2)
    print(nb)
    if nb >= 3:
        print(f"IP connectées plus de 3 fois : \nPremière connexion : ({element2}) \nDernière connexion : ({element2})")
        break
    
    print(f"nombre total de connexion uniques : {nb}")