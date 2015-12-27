import curses

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()

    # Text an bestimmten Koordinaten ausgeben:
    # Erster Parameter: Zeile, also y
    # Zweiter Parameter: Spalte, also x
    stdscr.addstr(0, 0, "Text an den Koordinaten y=0, x=0")
    stdscr.addstr(2, 20, "Text an den Koordinaten y=2, x=20")

    # curses.LINES gibt die Anzahl der Zeilen der aktuellen Konsole zurück.
    # curses.COLS die Anzahl der Spalten.
    # Folgender Befehl schreibt ein "X" ganz unten rechts in die Ecke.
    # (Falls die maximale Anzahl der Zeilen oder Spalten überschritten wird,
    #  kommt es zu einem Fehler: _curses.error: addwstr() returned ERR)
    stdscr.addstr(curses.LINES - 1, curses.COLS - 2, "X")

    # Gibt einen Text in der letzten Zeile aus
    stdscr.addstr(curses.LINES - 1, 0, "Taste zum Beenden drücken...")

    stdscr.getkey()

curses.wrapper(main)
