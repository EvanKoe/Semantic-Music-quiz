import curses
import math
from fetch import getTwentyRandomArtists
from display_themes import display_themes
from get_index_selected_theme import get_index_selected_theme

def main(argv):
    # init curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    stdscr.keypad(True)

    c = -1

    # random_artists = getTwentyRandomArtists()
    random_artists = [
        "TheWeekend", "Arianna Grande", "50 cent", "KIK", "Queen",
        "Vianney", "One Direction", "The Rolling Stones", "The Beatles", "The Who",
        "The Clash", "The Cure", "The Police", "The Smiths", "The Strokes",
        "The Velvet Underground", "The White Stripes", "The XX", "The Zombies", "The 1975",
    ]

    selected_artists = random_artists[:20] # To be sure there are maximum 20 artists
    number_of_artists = len(selected_artists)
    number_of_themes_by_line = 4

    lines = [selected_artists[i:i + number_of_themes_by_line] for i in range(0, number_of_artists, number_of_themes_by_line)]
    max_line_length = max(len(' '.join(line)) for line in lines)

    curses.init_pair(0, 255, 0) # id 0, white text, black background
    curses.init_pair(1, 0, 255) # id 1, black text, white background

    index_selected_theme = 0

    while c != ord('q'):
        stdscr.clear()

        maxY, maxX = stdscr.getmaxyx()

        if (maxY > (5 * math.ceil(number_of_artists / number_of_themes_by_line)) and maxX > max_line_length + number_of_themes_by_line):
            index_selected_theme = get_index_selected_theme(index_selected_theme, c, number_of_artists, number_of_themes_by_line)
            display_themes(stdscr, selected_artists, maxX, maxY, number_of_themes_by_line, index_selected_theme)
        else:
            strInfo = "Please enlarge the terminal"
            stdscr.addstr(maxY // 2, maxX // 2 - len(strInfo) // 2, strInfo)

        stdscr.refresh()

        c = stdscr.getch()

    # terminate curses
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

    return 0
