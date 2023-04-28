"""
Oppgave 3, oblig 7
Her importeres først klassen Sang fra sang.py. Oppretter så klassen Spilleliste med konstruktørparameter
listenavn. Definerer så instansvariablene sanger og navn. For denne første delen brukte jeg filen spilleliste.py
som lå ferdig på obligsiden. Det som er gjort videre har jeg selv kodet.

Metoden lesFraFil bruker en for-løkke til å åpne og lese fra filen vedlagt på obligsiden, musikk.txt. Den
leser linje for linje og deler opp ved semikolon, mellom artist og tittel på sang. Derettet legger vi til
verdiene artist og tittel som parametere i klassen Sang, og dette blir en sang.
Metoden leggTilSang har parameter nySang og legger til en ny sang i listen sanger med append metoden.
Metoden fjernSang gjør da det motsatte, ved hjelp av metoden remove.
Metoden spillSang tar med parameter sang og spiller av sangen ved hjelp av metoden spill fra klassen Sang.
Metoden spillAlle kjører en for løkke gjennom listen sanger og spiller hvert element med den samme metoden
spill.
Metoden finnSang tar med parameten tittel og itererer gjennom lista sanger ved hjelp av en for-løkke. For alle
elementene i lista returneres navnet på elementet. Her implementeres også metoden sjekkTittel fra klassen Sang
og vi sjekker med en if-test om en gitt tittel er lik instansvariabelen tittel. Isåfall returneres elementet
som skal være likt. Hvis ikke returneres None.
siste metode hentArtistUtvalg tar med parameteren artistnavn og en tom liste artistutvalg. Vi itererer igjen
gjennom listen sanger med en for-løkke. For hvert element i lista legges artistnavnene inn i lista
artistutvalg ved bruk av metoden sjekkArtist fra klassen Sang. Til slutt returneres artistutvalg, som nå
består av alle artistnavnene.
"""
from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        for linje in open(filnavn):
            data = linje.strip().split(";")
            artist = data[0]
            tittel = data[1]
            self._sanger.append(Sang(artist, tittel))
            #LUKK FILEN fil.close()

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for x in self._sanger:
            x.spill()

    def finnSang(self, tittel):
        for x in self._sanger:
            return x
            if x.sjekkTittel(tittel) == True:
                return x
        return none

    def hentArtistUtvalg(self, artistnavn):
        artistutvalg = []
        for x in self._sanger:
            if x.sjekkArtist(artistnavn):
                artistutvalg.append(x)
        return artistutvalg
