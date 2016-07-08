#!/usr/bin/python3

"""
Das Stein-Papier-Schere-Spiel
"""

import sys
import os
from getch import *

###############################################################################
### Funktionen
###############################################################################

def taste_zu_spieler(tasten, k):
    if k.upper() in tasten[0]:
        return 0
    elif k.upper() in tasten[1]:
        return 1
    else:
        return -1

def taste_zu_objekt(tasten, k):
    k = k.upper() # Großbuchstabe

    if k in tasten[0]:
        return tasten[0].index(k)
    elif k in tasten[1]:
        return tasten[1].index(k)
    else:
        return -1

def gewinn_aktion(obj0, obj1):
    """
    Liefert den Text wie obj0 über obj1 gewinnt.
    Wenn obj0 gegenüber obj1 verliert, wird "ungültig" geliefert
    """
    if obj0 == 0 and obj1 == 2:
        return "Stein macht Schere stumpf."
    if obj0 == 1 and obj1 == 0:
        return "Papier umwickelt Stein."
    if obj0 == 2 and obj1 == 1:
        return "Schere zerschneidet Papier."

    return "ungültig"

def auswertung(obj0, obj1):
    """
    obj0 gehört zu spieler0.
    obj1 gehört zu spieler1.

    Liefert zurück, wer gewonnen hat (0 oder 1) oder -1 für unentschieden
    """
    if obj0 == 0 and obj1 == 2 or obj0 == 1 and obj1 == 0 or obj0 == 2 and obj1 == 1:
        return 0
    elif obj1 == 0 and obj0 == 2 or obj1 == 1 and obj0 == 0 or obj1 == 2 and obj0 == 1:
        return 1
    else:
        return -1

def ready(tasten):
    print("Ready... ", end="")
    sys.stdout.flush() # damit die Ausgabe sofort erscheint

    k0 = getch()
    k1 = getch()

    s0 = taste_zu_spieler(tasten, k0)
    s1 = taste_zu_spieler(tasten, k1)

    if s0 >= 0 and s1 >= 0 and s0 != s1:
        print("OK\n")
    else:
        print("!Ungültig!")

def fight(tasten, spieler, objekte, punkte, bilder):
    print("Go...")
    print("")

    k0 = getch()
    k1 = getch()

    s0 = taste_zu_spieler(tasten, k0)
    s1 = taste_zu_spieler(tasten, k1)

    if s0 >= 0 and s1 >= 0 and s0 != s1:
        obj0 = taste_zu_objekt(tasten, k0)
        obj1 = taste_zu_objekt(tasten, k1)

        if s0 == 1:
            swap = obj1
            obj1 = obj0
            obj0 = swap

        print("{0:40}{1:40}".format(spieler[0], spieler[1]))
        print("{0:40}{1:40}".format("v", "v"))
        print("{0:40}{1:40}".format(objekte[obj0], objekte[obj1]))
        print("-" * 80)

        s = auswertung(obj0, obj1)
        if s >= 0:

            if s == 0:
                print_bild(bilder, obj0, 0)
            else:
                print_bild(bilder, obj1, 40)

            # Punktestand anpassen
            punkte[s] = punkte[s] + 1

            ga = None
            if s == 0:
                ga = gewinn_aktion(obj0, obj1)
            else:
                ga = gewinn_aktion(obj1, obj0)
            print(">> {0} hat gewonnen, denn {1}".format(spieler[s], ga))
        else:
            print(">> UNENTSCHIEDEN")

        print("                    Punktestand:")
        print("{0:40}{1:40}".format(spieler[0] + " ({0})".format(punkte[0]), spieler[1] + " ({0})".format(punkte[1])))

    else:
        print("!Ungültig!")

def hole_spielernamen():
    spieler0 = None
    spieler1 = None

    if len(sys.argv) == 3:
        spieler0 = sys.argv[1]
        spieler1 = sys.argv[2]
    else:
        print("Bitte Namen per Hand eintragen.")
        spieler0 = input("Spieler 1: ")
        spieler1 = input("Spieler 2: ")
        print("")

    return [ spieler0, spieler1 ]

def lade_bilder():
    bilder = []
    with open('sp-data/stein.txt') as f:
        bilder.append(f.read())

    with open('sp-data/papier.txt') as f:
        bilder.append(f.read())

    with open('sp-data/schere.txt') as f:
        bilder.append(f.read())

    return bilder

def print_bild(bilder, obj, offset = 0):
    if offset == 0:
        print(bilder[obj])
    else:
        bild = bilder[obj]
        zeilen = bild.split(os.linesep)
        for z in zeilen:
            print(" " * offset + z)

###############################################################################
### main
###############################################################################

def main():
    print("     ------------------------------------")
    print("     Hallo zum Stein-Papier-Schere-Spiel.")
    print("     ------------------------------------")
    print("")

    objekte = [ "Stein", "Papier", "Schere" ]

    # erste Zeile für Spieler 1 und zweite Zeile für Spieler 2
    tasten = [ [ 'A', 'S', 'D' ],
               [ 'J', 'K', 'L' ]
            ]

    punkte = [ 0, 0 ]

    bilder = lade_bilder()

    spieler = hole_spielernamen()

    print("{0:40}{1:40}".format("Spieler 1", "Spieler 2"))
    print("{0:40}{1:40}".format("---------", "---------"))
    print("{0:40}{1:40}".format(spieler[0], spieler[1]))
    print("")

    print("                       Tasten:\n")

    for i in range(3):
        print("{0} = {1:36}{2} = {3:36}".format(tasten[0][i], objekte[i], tasten[1][i], objekte[i]))
    print("")

    print("Spielverlauf:")
    print("   1. Jeder Spieler drückt eine seiner Tasten zur Vorbereitung.")
    print("   2. Nochmal Vorbereitung")
    print("   3. Jeder Spieler drückt die Taste, mit der er seinen Gegenspieler herausfordert.")
    print("")

    ready(tasten)
    ready(tasten)
    fight(tasten, spieler, objekte, punkte, bilder)
    print("")

if __name__ == "__main__":
    main()

