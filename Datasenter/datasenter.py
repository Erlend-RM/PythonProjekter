from node import Node
from rack import Rack
from regneklynge import Regneklynge


class Datasenter:


	# Oppretter et datasenter
    def __init__(self):
        self._datasenter = {}


	# Leser inn data om en regneklynge fra fil og legger den til i ordboken
    def lesInnRegneklynge(self, filnavn):
        fil = open(filnavn)
        noderPerRack = int(fil.readline())
        regneklynge = Regneklynge(noderPerRack)
        for linje in fil:
            deler = linje.strip().split()
            antallNoder = int(deler[0])
            minne = int(deler[1])
            antPros = int(deler[2])
            for x in range(antallNoder):
                node = Node(minne, antPros)
                regneklynge.settInnNode(node)
        self._datasenter[filnavn] = regneklynge


	# Skriver ut informasjon om alle regneklyngene
    def skrivUtAlleRegneklynger(self):
        for objekt in self._datasenter:
            self.skrivUtRegneklynge(objekt)


	# Skriver ut informasjon om en spesifikk regeklynge
    def skrivUtRegneklynge(self, navn):
        snavn = navn.strip(".txt")
        print(f"Informasjon om regneklynge {snavn}")
        print(f"Antall rack: {self._datasenter[navn].antRacks()}")
        print(f"Antall prosessorer: {self._datasenter[navn].antProsessorer()}")
        print(f"Noder med minst 32GB: {self._datasenter[navn].noderMedNokMinne(32)}")
        print(f"Noder med minst 64GB: {self._datasenter[navn].noderMedNokMinne(64)}")
        print(f"Noder med minst 128GB: {self._datasenter[navn].noderMedNokMinne(128)}\n")
