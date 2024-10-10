trame_meteo = "$METEO,22.5C,55%,1013hPa,Clair"

tab = trame_meteo.split(",")

if tab[0] == "$METEO" and len(tab != 5):
    temp = (tab[1].replace("C", "")) #trame_meteo.split (",") [1]
    humidite = (tab[2].replace("%", "")) #trame_meteo.split (",") [2]
    pression = (tab[3].replace("hPa", "")) #trame_meteo.split (",") [3]

    print("Température :", temp ,"C")
    print("Humidité :", humidite ,"%")
    print("Pression atmosphérique :", pression ,"hPa")
else:
    print("Erreur la trame ne respecte pas le format")
