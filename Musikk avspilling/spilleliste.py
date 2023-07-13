#Importerer Sang her for å kunne bruke denne i Spilleliste
from sang import Sang

#Setter klassen Spilleliste
class Spilleliste:

#Lager init for klassen
#Listenavn må være med for å kunne et spilleliste objekt.
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

#STR for klassen slik at når man printer i Spilleliste
#så får man navnet på spillelisten.
    def __str__(self):
        return f"Spilleliste: {self._navn}"

#Funksjonen som brukes for å lese data fra fil
    def lesFraFil(self, filnavn):
        spilleListe = open(filnavn)
        for linje in spilleListe:
            alleData = linje.strip().split(";")
            nySang = Sang(alleData[1],alleData[0])
            self._sanger.append(nySang)

#Denne funksjonen legger til sang i spillelisten
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

#Denne funksjonen fjerner sang i spillelisten
    def fjernSang(self, sang):
        self._sanger.remove(sang)

#Denne funksjonen spiller sang i spillelisten
    def spillSang(self, sang):
        Sang.spill(sang)

#Denne funksjonen spiller alle sang i spillelisten.
    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

#Denne funksjonen finner sang i spillelisten utifra tittel.
    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang

#Denne funksjonen henter ut sanger som har samme artist.
    def hentArtistUtvalg(self, artistnavn):
        listForArtist = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                listForArtist.append(sang)
        return listForArtist
