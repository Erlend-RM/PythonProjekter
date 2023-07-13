from node import Node


class Rack:

    # oppretter et rack der det senere kan plasseres node
    def __init__(self):
        self._rack = []


    # Plasserer en ny node inn i racket
    def settInn(self, node):
        self._rack.append(node)


	# Henter antall noder i racket
    def getAntNoder(self):
        antallNoder = len(self._rack)
        return antallNoder


	# Beregner sammenlagt antall prosessorer i nodene i et rack
    def antProsRack(self):
        totAntProsRack = 0
        for linje in self._rack:
            totAntProsRack += Node.antProsNode(linje)
        return totAntProsRack


	# Beregner antall noder i racket med minne over en gitt grense
    def noderMedNokMinne(self, paakrevdMinne):
        noderMedNokMinne = 0
        for linje in self._rack:
            if True == linje.nokMinne(paakrevdMinne):
                noderMedNokMinne += 1
        return noderMedNokMinne
