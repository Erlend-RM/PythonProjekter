
#Her defineres klassen Sang
class Sang:

#Her er init til klassen satt, Artist og Tittel må være
#med for å kunne lage et sang objekt.
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

#STR for klassen slik at når man printer sang så får man tittel og artist.
    def __str__(self):
        return f"Tittel: '{self._tittel}' Artist: '{self._artist}'"

#Spill funksjonen er for å vise hvilken sang som spilles.
    def spill(self):
        print(f"Spiller: '{self._tittel}' by '{self._artist}'.")

#Denne funksjonen sjekker om artisten er i sangen.
#Den sjekker også om et ord i artistnavnet er der.
#Returner True om deler av artistnavnet er der.
    def sjekkArtist(self, navn):
        listeMedNavn = navn.split()
        listArtist = self._artist.split()
        for ord in listeMedNavn:
            if ord in listArtist:
                return True

#Denne fuksjonen sjekker om deler av tittelen er der.
#Returner True om deler av tittel er der.
    def sjekkTittel(self, tittel):
        lowTittel = tittel.lower()
        listeTittel = lowTittel.split()
        _tittel = self._tittel.lower()
        liste_Titel = _tittel.split()
        for delAvTittel in listeTittel:
            if delAvTittel in liste_Titel:
                return True

#Denne funksjonen sjekker om deler av artist eller tittel er der.
#Returner True om en det er en del av begge er der.
    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist) == True and self.sjekkTittel(tittel) == True:
            return True
