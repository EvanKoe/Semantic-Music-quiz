import curses
import math

def display_items(stdscr, items: list, maxX: int, maxY: int, number_of_items_by_line: int, index_selected_item: int):
    number_of_lines = math.ceil(len(items) / number_of_items_by_line)
    middle_height = maxY // 2
    middle_width = maxX // 2
    length_line = 0

    i = 0
    k = 0
    while i < number_of_lines:
        yStartStr = middle_height - (number_of_lines // 2) * 5 + i * 5
        for j in range(number_of_items_by_line):
            if k + j < len(items):
                length_line += len(items[k + j])
                if j > 0:
                    length_line += 2
        xStartStr = middle_width - length_line // 2

        for j in range(number_of_items_by_line):
            if k < len(items):
                if k == index_selected_item:
                  stdscr.addstr(yStartStr, xStartStr, items[k], curses.color_pair(1))
                else:
                  stdscr.addstr(yStartStr, xStartStr, items[k], curses.color_pair(0))
                xStartStr += len(items[k]) + 2
                k += 1

        length_line = 0
        i += 1
