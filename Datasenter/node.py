class Node:


    # Oppretter en node med gitt minne-størrelse og antall prosessorer
    def __init__(self, minne, antPros):
        self._minne = minne
        self._antPros = antPros

    #Skriver ut minne-størrelse og antall prosessorer for noden
    def __str__(self):
        return f"Minne-storrelsen: {self._minne}GB \nAntall prosessorer: {self._antPros}"


	# Henter antall prosessorer i noden og returner disse
    def antProsNode(self):
        return self._antPros


	# Sjekker om noden har tilstrekkelig minne for et program
    def nokMinne(self, paakrevdMinne):
        if paakrevdMinne <= self._minne:
            return True
