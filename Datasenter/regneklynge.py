from node import Node
from rack import Rack


class Regneklynge:

    # Oppretter en regneklynge og setter maks antall noder det er plass til i et rack
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._regneklynge = []

    #Skriver ut maks antall noder i rack.
    def __str__(self):
        return f"Maks antall noder i rackene: {self._noderPerRack}"


	# Plasserer en node inn i et rack med ledig plass, eller i et nytt om det er fult.
    def settInnNode(self, node):
        ledig = False
        for rackInRegn in self._regneklynge:
            if rackInRegn.getAntNoder() < self._noderPerRack:
                rackInRegn.settInn(node)
                ledig = True
        if not ledig:
            nyttRack = Rack()
            nyttRack.settInn(node)
            self._regneklynge.append(nyttRack)


	# Beregner totalt antall prosessorer i hele regneklyngen
    def antProsessorer(self):
        totAntProsRegn = 0
        for linje in self._regneklynge:
            totAntProsRegn += linje.antProsRack()
        return totAntProsRegn


	# Beregner antall noder i regneklyngen med minne over en gitt grense.
    def noderMedNokMinne(self, paakrevdMinne):
        antallMedNokM = 0
        for linje in self._regneklynge:
            antallMedNokM += linje.noderMedNokMinne(paakrevdMinne)
        return antallMedNokM


	# Henter antall racks i regneklyngen og returner disse.
    def antRacks(self):
        antallRack = len(self._regneklynge)
        return antallRack
