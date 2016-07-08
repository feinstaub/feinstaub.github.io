#!/usr/bin/python3

"""
Das Stein-Papier-Schere-Spiel
"""

import sys
from getch import *

###############################################################################
### Globale Variablen

objekte = [ "Stein", "Papier", "Schere" ]

# erste Zeile für Spieler 1 und zweite Zeile für Spieler 2
tasten = [ [ 'A', 'S', 'D' ],
           [ 'J', 'K', 'L' ]
         ]

###############################################################################
### Funktionen                                                              ###

def taste_zu_spieler(k):
    if k.upper() in tasten[0]:
        return 0
    elif k.upper() in tasten[1]:
        return 1
    else:
        return -1

def taste_zu_objekt(k):
    k = k.upper() # Großbuchstabe

    if k in tasten[0]:
        return tasten[0].index(k)
    elif k in tasten[1]:
        return tasten[1].index(k)
    else:
        return -1

###############################################################################

print("------------------------------------")
print("Hallo zum Stein-Papier-Schere-Spiel.")
print("------------------------------------")
print("")

spieler1 = "Kurt"
spieler2 = "Lea"

spieler = [ spieler1, spieler2 ]

print("Spieler 1                           Spieler 2")
print("{0}                                {1}".format(spieler[0], spieler[1]))
print("")

print("Es gelten folgende Tasten:")
print("")
print("{0} = {1}                           {2} = {3}".format(tasten[0][0], objekte[0], tasten[1][0], objekte[0]))
print("{0} = {1}                          {2} = {3}".format(tasten[0][1], objekte[1], tasten[1][1], objekte[1]))
print("{0} = {1}                          {2} = {3}".format(tasten[0][2], objekte[2], tasten[1][2], objekte[2]))
print("")

print("Tastentest \n   - Jeder Spieler drückt seine Tasten (gerne auch ungültige Tasten):")
print("   - Q zum Beenden")
print("")

while True:
    k = getch()
    s = taste_zu_spieler(k)
    if s >= 0:
        o = taste_zu_objekt(k)
        print("Die Taste gehört zum {0} von {1}".format(objekte[o], spieler[s]))
    else:
        print("Taste: " + k)
    if k == 'q':
        print("Beenden...")
        break
