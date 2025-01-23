class WeatherStation ():
    def __init__(self, temperature, pression, humidite):
        self._temperature = temperature
        self._pression = pression
        self._humidite = humidite
    
    def temperature(self):
        return self._temperature
    
    def pression(self):
        return self._pression
    
    def humidite(self):
        return self._humidite
    
    def temperature(self, value: float):
        self._temperature = value

    def pression(self, value: float):
        self._pression = value

    def humidite(self, value: int):
        self._humidite = value

    def convert_temperature(self):
        return(self._temperature - 32) * 5/9
    def convert_pressure(self):
        return self.pression / 100000
    
    def affichage(self):
        print(f"Temperature: {self._temperature} °F et {self.convert_temperature():.2f} °C")
        print(f"Pression: {self._pression} Pascal et {self.convert_pressure():.2f} Bar")
        print(f"Humidité: {self._humidite}%")

    def __doc__():
        return

    def getattr():
        return
    
    def str():
        return