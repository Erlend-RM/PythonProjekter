class Motorsykkel:

    def __init__(self, merke, registreringsnummer, kilometerstand):
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._kilometerstand = kilometerstand

    def kjor(self, km):
        self._kilometerstand += km

    def hentKilometerstand(self):
        return self._kilometerstand

    def skrivUt(self):
        print(self._merke)
        print(self._registreringsnummer)
        print(self._kilometerstand)
