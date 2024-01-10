import curses

def get_index_selected_theme(index_selected_theme: int, c: int, number_of_themes: int, number_of_themes_by_line: int):
    if c == curses.KEY_LEFT:
        index_selected_theme = index_selected_theme - 1 if index_selected_theme > 0 else number_of_themes - 1
    elif c == curses.KEY_RIGHT:
        index_selected_theme = index_selected_theme + 1 if index_selected_theme < number_of_themes - 1 else 0
    elif c == curses.KEY_UP:
        index_selected_theme = index_selected_theme - number_of_themes_by_line if index_selected_theme - number_of_themes_by_line >= 0 else number_of_themes - number_of_themes_by_line + index_selected_theme
    elif c == curses.KEY_DOWN:
        index_selected_theme = index_selected_theme + number_of_themes_by_line if index_selected_theme < number_of_themes - number_of_themes_by_line else index_selected_theme % number_of_themes_by_line
    return index_selected_theme
