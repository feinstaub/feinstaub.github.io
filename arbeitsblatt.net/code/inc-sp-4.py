#!/usr/bin/python3

"""
Das Stein-Papier-Schere-Spiel
"""

import sys

###############################################################################
### Damit wir Tasten auslesen können.                                       ###

class _Getch:
    # found on http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/

    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()

###############################################################################
### Globale Daten                                                           ###

objekte = { 0: "Stein", 1: "Papier", 2: "Schere" }

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
    print("Taste: " + k)
    s = taste_zu_spieler(k)
    if s >= 0:
        print("Die Taste gehört zu {0}".format(spieler[s]))
    if k == 'q':
        print("Beenden...")
        break
