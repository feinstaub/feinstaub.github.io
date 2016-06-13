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

print("------------------------------------")
print("Hallo zum Stein-Papier-Schere-Spiel.")
print("------------------------------------")
print("")

spieler1 = "Kurt"
spieler2 = "Lea"

print("Spieler 1                           Spieler 2")
print("{0}                                {1}".format(spieler1, spieler2))
print("")

print("Es gelten folgende Tasten:")
print("")
print("A = Stein                           J = Stein")
print("S = Schere                          K = Schere")
print("D = Papier                          L = Papier")
print("")

print("Tastentest \n   - Jeder Spieler drückt seine Tasten (gerne auch ungültige Tasten):")
print("   - Q zum Beenden")
print("")

while True:
    k = getch()
    print("Taste: " + k)
    if k == 'q':
        break
