import curses

def main(stdscr):

    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(False)

    i = 0

    # Attribute setzen

    stdscr.addstr(i, 0, "Attribut: keins"); i += 1
    stdscr.addstr(i, 0, "Attribut: A_REVERSE", curses.A_REVERSE); i += 1
    stdscr.addstr(i, 0, "Attribut: A_BOLD", curses.A_BOLD); i += 1
    stdscr.addstr(i, 0, "Attribut: A_DIM (oft äquivalent zu keins)", curses.A_DIM); i += 1
    stdscr.addstr(i, 0, "Attribut: A_BLINK", curses.A_BLINK); i += 1
    stdscr.addstr(i, 0, "Attribut: A_STANDOUT (oft äquivalent zu A_BOLD)", curses.A_STANDOUT); i += 1
    stdscr.addstr(i, 0, "Attribut: A_UNDERLINE", curses.A_UNDERLINE); i += 1

    i += 1 # Leere Zeile

    # Farben setzen.
    #
    # Farben kann man immer nur in der Kombination
    # Text- und Hintergrundfarbe setzen.
    # Diese Kombination wird in einer color_pair-Nummer > 0 registriert.

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.addstr(i, 0, "Farbe: COLOR_RED", curses.color_pair(1))
    i += 1

    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    stdscr.addstr(i, 0, "Farbe: COLOR_BLUE", curses.color_pair(2))
    i += 1

    colors = [ curses.COLOR_CYAN, curses.COLOR_GREEN, curses.COLOR_MAGENTA,
               curses.COLOR_WHITE, curses.COLOR_YELLOW ]

    for ci, col in enumerate(colors):
        col_pair_num = ci + 3
        curses.init_pair(col_pair_num, col, curses.COLOR_BLACK)
        stdscr.addstr(i, 0, "Farbe: {}".format(col), curses.color_pair(col_pair_num))
        i += 1

    i += 1 # Leere Zeile

    # Kombination aus Attributen und Farben.
    # HINWEIS: Nicht alle Kombinationen aus Attributen und Farben funktionieren.

    # color_pair-Nummer 1 von oben
    stdscr.addstr(i, 0, "Farbe und Blinken 1", curses.color_pair(1) + curses.A_BLINK); i += 1

    curses.init_pair(9, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    stdscr.addstr(i, 0, "Farbe und Blinken 2", curses.color_pair(9) + curses.A_BLINK); i += 1

    stdscr.addstr(curses.LINES - 1, 0, "Taste zum Beenden drücken...")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
