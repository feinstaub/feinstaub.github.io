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

def ready():
    print("Ready...")
    k0 = getch()
    k1 = getch()

    s0 = taste_zu_spieler(k0)
    s1 = taste_zu_spieler(k1)

    if s0 >= 0 and s1 >= 0 and s0 != s1:
        print("        OK")
    else:
        print("!Ungültig!")

def fight():
    print("Go...")
    k0 = getch()
    k1 = getch()

    s0 = taste_zu_spieler(k0)
    s1 = taste_zu_spieler(k1)

    if s0 >= 0 and s1 >= 0 and s0 != s1:
        obj0 = taste_zu_objekt(k0)
        obj1 = taste_zu_objekt(k1)

        if s0 == 1:
            swap = obj1
            obj1 = obj0
            obj0 = swap

        print("         {0}                                {1}".format(spieler[0], spieler[1]))
        print("      # {0} #                           # {1} #".format(objekte[obj0], objekte[obj1]))
    else:
        print("!Ungültig!")



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
for i in range(3):
    print("{0} = {1}                           {2} = {3}".format(tasten[0][i], objekte[i], tasten[1][i], objekte[i]))
print("")

print("Spielverlauf:")
print("   - Jeder Spieler drückt eine seiner Tasten zur Vorbereitung.")
print("   - Jeder Spieler nochmal drückt eine seiner Tasten zur Vorbereitung.")
print("   - Jeder Spieler drückt die Taste, mit der er seinen Gegenspieler herausfordert.")
print("")

ready()
ready()
fight()
