#!/usr/bin/python3
# -*- coding: utf-8 -*-

import curses
import math
import time

def get_kessel_numbers():
    rot = [ 32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3 ]
    schwarz = [ 15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26 ]

    numbers = [ 0 ]
    for (r, s) in zip(rot, schwarz):
        numbers = numbers + [ r, s ]

    return numbers

def main(stdscr):

    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(False)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN) # grünes Feld
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)   # rotes Feld
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # schwarzes Feld
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK) # Kugel

    numbers = get_kessel_numbers()

    num_dots = 37
    ratio = 18 / 10

    ox = 70
    oy = 20

    rx = 30
    ry = rx / ratio
    for i in range(0, num_dots):
        #                                damit oben in der Mitte begonnen wird
        phi = 2 * math.pi / num_dots * i - math.pi / 2
        x = round(math.cos(phi) * rx + ox)
        y = round(math.sin(phi) * ry + oy)
        col_pair = curses.color_pair(1)
        if i > 0:
            col_pair = curses.color_pair(i % 2 + 2)
            col_pair += curses.A_BOLD
            if i % 2 == 1:
                col_pair += curses.A_UNDERLINE
        stdscr.addstr(y, x, "{0: ^4}".format(numbers[i]), col_pair)

        #time.sleep(0.02)
        time.sleep(2 / ((i+1) * 10))

        stdscr.refresh()

    rx = 26
    ry = rx / ratio
    for i in reversed(range(0, num_dots)):
        #                                damit oben in der Mitte begonnen wird
        phi = 2 * math.pi / num_dots * i - math.pi / 2
        x = round(math.cos(phi) * rx + ox + 1)
        y = round(math.sin(phi) * ry + oy)
        stdscr.addstr(y, x, "o", 4)

        #time.sleep(0.02)
        time.sleep(2 / ((i+1) * 10))

        stdscr.refresh()


    stdscr.addstr(curses.LINES - 1, 0, "Taste zum Beenden drücken...")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)

# print(get_kessel_numbers())
