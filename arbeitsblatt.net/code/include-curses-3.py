import curses

# globale Variable
debugstr = ""

def main(stdscr):

    # Globale Variable innerhalb der Funktion bekannt machen
    # (ansonsten ist sie lokal).
    global debugstr

    stdscr.clear()
    stdscr.refresh()

    # Cursor ausblenden, wenn nicht benötigt.
    curses.curs_set(False)

    # Ein Fenster mit einer bestimmten Größe und Position erzeugen.
    begin_x = 5
    begin_y = 3
    height = 10
    width = 35
    win = curses.newwin(height, width, begin_y, begin_x)

    # Attribute des win-Objekts auflisten und dem debugstr zuweisen.
    debugstr = str(dir(win))

    # Das Fenster soll einen Rahmen haben.
    win.border()

    # Das Fenster mit Buchstaben füllen.
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            win.addch(y, x, ord('a') + (x - 1) % 26)

    # Refresh, ansonsten wird der Fensterhinhalt nicht angezeigt.
    win.refresh()

    stdscr.addstr(curses.LINES - 1, 0, "Taste zum Beenden drücken...")
    stdscr.getkey()

curses.wrapper(main)

# Nach Beenden des Programms kann man die Debug-Nachricht auf der Konsole lesen.
print(debugstr)
