trame_meteo = "$METEO,22.5C,55%,1013hPa,Clair"

tab = trame_meteo.split(",")

if tab[0] == "$METEO" :
    temp = trame_meteo.split (",") [1]
    humidite = trame_meteo.split (",") [2]
    pression = trame_meteo.split (",") [3]

    print("Température :", temp)
    print("Humidité :", humidite)
    print("Pression atmosphérique :", pression)
else:
    print("Erreur la trame ne respecte pas le format")
