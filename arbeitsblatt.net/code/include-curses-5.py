import curses

def main(stdscr):

    stdscr.clear()
    stdscr.refresh()

    prompt = "Bitte Text eingeben: "
    stdscr.addstr(0, 0, prompt)

    # Wenn Tasten gedrückt werden, dann sollen diese auch sichtbar sein.
    curses.echo()

    # Liest einen String mit der maximalen Länge 15 ein.
    # Der zurückgegebe Wert ist ein byte-String, der mit
    # der decode-Funktion in einen normalen String konvertiert
    # wird.
    s = stdscr.getstr(0, len(prompt), 15).decode("utf-8")

    # Ausgabe von gedrückten Tasten wieder abstellen.
    curses.noecho()

    stdscr.addstr(1, 0, "Der Text war '{}'.".format(s))

    stdscr.addstr(curses.LINES - 1, 0, "Taste zum Beenden drücken...")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
