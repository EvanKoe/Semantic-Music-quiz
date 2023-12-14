#!/usr/bin/env python3

import sys
import curses
import math

def display_themes(stdscr, themes: list, maxX: int, maxY: int):
    number_of_lines = math.ceil(len(themes) / 3)
    middle_height = maxY // 2
    middle_width = maxX // 2
    length_line = 0

    i = 0
    k = 0
    while i < number_of_lines:
        yStartStr = middle_height - (number_of_lines // 2) * 5 + i * 5
        if k < len(themes):
            length_line += len(themes[k])
        if k + 1 < len(themes):
            length_line += len(themes[k + 1]) + 2
        if k + 2 < len(themes):
            length_line += len(themes[k + 2]) + 2
        xStartStr = middle_width - length_line // 2

        if k < len(themes):
            stdscr.addstr(yStartStr, xStartStr, themes[k])
            k += 1
        if k < len(themes):
            stdscr.addstr(yStartStr, xStartStr + len(themes[k - 1]) + 2, themes[k])
            k += 1
        if k < len(themes):
            stdscr.addstr(yStartStr, xStartStr + len(themes[k - 2]) + len(themes[k - 1]) + 4, themes[k])
            k += 1
        length_line = 0
        i += 1

def main(argv):
    # init curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    c = -1

    while c != ord('q'):
        stdscr.clear()

        maxY, maxX = stdscr.getmaxyx()

        if (maxY > 20 and maxX > 60):
            display_themes(stdscr, ["Theme 1", "Theme 2", "Theme 3", "Theme 4", "Theme 5", "Theme 6", "Theme 7", "Theme 8"], maxX, maxY)
        else:
            strInfo = "Please enlarge the window"
            stdscr.addstr(maxY // 2, maxX // 2 - len(strInfo) // 2, strInfo)

        stdscr.refresh()

        c = stdscr.getch()

    # terminate curses
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

    return 0
