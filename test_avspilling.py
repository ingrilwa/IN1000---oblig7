"""
Oppgave 4, oblig 7 - Frivillig oppgave med avspilling av sanger

Vi importerer klassene Sang og Spilleliste.
Så definerer vi et hovedprogram. Jeg legger til to objekter, sang2 og sang3 med artistnavn, tittel og filnavn
som legges til i klassen Sang. Så spiller jeg av sangene ved hjelp av metoden spill fra klassen Sang.
Jeg lastet ned simpleaudio og la til lydfilene (fra lydfiler.zip fra obligsiden) i samme mappe som disse
filene. Importerte biblioteket fra simpleaudio i klassen Sang. Siste del av oppgaven sa at jeg skulle legge
til sangene i en spilleliste og så bruke metoden spillAlle for å spille av hele lista. Deretter lagde jeg en
ny spilleliste kalt nyMusikk og la til sangene sang2 og sang3 ved hjelp av metoden leggTilSang. Så printer
jeg ut at jeg tester lista og spiller alle sangene i lista. Til slutt bruker jeg metoden spillAlle og begge
sangene i lista spilles på macen min når jeg kjører koden i terminal for å teste. Til slutt kaller jeg på
hovedprogram.

For at denne skal fungere må de ekstra opplysningene som filnavn og koden inni metoden spill() tas med. For at
de andre testprogrammene skulle fungere fint uten feilmeldinger kommenterte jeg noe av koden ut. Denne koden
må settes inn igjen, ta bort kommentartegnene i koden i filen sang.py, for at dette tilleggsprogrammet skal fungere.
"""

from sang import Sang
from spilleliste import Spilleliste

def hovedprogram():
    sang2 = Sang("Albinoni", "Adagio", "adagio.wav")
    sang3 = Sang("Beethoven", "Ode to Joy", "ode_to_joy.wav")

    #sang2.spill()
    #sang3.spill()

    nyMusikk = Spilleliste("nye sanger")
    nyMusikk.leggTilSang(sang2)
    nyMusikk.leggTilSang(sang3)
    print("Tester nyMusikk: Spiller alle sanger i listen:")
    nyMusikk.spillAlle()


hovedprogram()
