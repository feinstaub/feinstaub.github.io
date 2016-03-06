import curses

def main(stdscr):
    # Bildschirm löschen; am Anfang nicht unbedingt notwendig.
    stdscr.clear()

    # Aufgrund einer Eigenheit der curses-Bibliothek
    # ist folgendes refresh notwendig, sonst funktionieren
    # einige Befehle nicht wie erwartet.
    stdscr.refresh()

    # Text auf Bildschirm ausgeben
    stdscr.addstr(0, 0, "Taste zum Beenden drücken...")

    # Warte auf beliebigen Tastendruck, bevor die
    # Konsole wieder aufgeräumt und das Programm beendet wird.
    stdscr.getkey()

# main-Funktion mit dem Wrapper starten.
# Der Wrapper sorgt für nötige Initialisierungen
# und Aufräumarbeiten im Fehlerfall.
curses.wrapper(main)
