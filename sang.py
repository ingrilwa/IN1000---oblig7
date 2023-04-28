"""
Oppgave 2, oblig 7.
Jeg har opprettet en klasse Sang. Konstruktøren har parameterne artist og tittel, og etter utvidelser gjort i
oppgave 4, har jeg også med parameteren filnavn. Jeg har også derfor importert simpleaudio, som gjør at sangene
i oppgave 4 spilles av. Videre oppretter konstruktøren instansvariablene tittel, artist og filnavn.

Metoden spill "spilte" først av musikken som testes i testSang, men jeg gjorde utvidelser og endret programmet
som sagt, så nå spiller den faktisk av sangen. Koden i spill er kopiert fra oppgaveteksten i oppgave 4.

Metoden sjekkArtist tar parameter navn og returnerer True dersom en del av navn finnes i artistnavnet.
Metoden sjekkTittel tar parameter tittel og returnerer True dersom den oppgitte tittelen er lik instansvariabelen
tittel. Dette skjer uavhengig av små eller store bokstaver, da jeg bruker .lower()
Metoden sjekkArtistOgTittel tar både parameter artist og tittel og returnerer True dersom både artist og tittel
er det samme som sangens instansvariabler.
"""

import simpleaudio as sa

class Sang:

    def __init__ (self, artist, tittel): #,filnavn):
        self._tittel = tittel
        self._artist = artist
        #self._filnavn = filnavn

    def spill(self):
        print("Spiller", self._tittel, "av", self._artist)
        #wave_obj = sa.WaveObject.from_wave_file(self._filnavn)
        #play_obj = wave_obj.play()
        #play_obj.wait_done()


    def sjekkArtist(self, navn):
        for x in navn.split(" "):
            if x in self._artist.split(" "):
                return True
        return False

    def sjekkTittel(self, tittel):
            return tittel.lower()== self._tittel.lower()

    def sjekkArtistOgTittel(self, artist, tittel):
        return self.sjekkTittel(tittel) and self.sjekkArtist(artist)
