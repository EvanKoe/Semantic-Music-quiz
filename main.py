import curses
import math
from fetch import getTwentyRandomArtists
from display_items import display_items
from get_index_selected_item import get_index_selected_item
from display_questions import display_questions
from fake_data import fake_artists, fake_questions

def main(argv):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    stdscr.keypad(True)

    c = -1

    selected_artists = fake_artists[:20] # To be sure there are maximum 20 artists
    number_of_artists = len(selected_artists)
    number_of_themes_by_line = 4

    max_length = max(len(artist) for artist in selected_artists)
    artists = [f"{artist.center(max_length)}" for artist in selected_artists] # fill of spaces to have the same length

    lines = [artists[i:i + number_of_themes_by_line] for i in range(0, number_of_artists, number_of_themes_by_line)]
    max_line_length = max(len(' '.join(line)) for line in lines)

    curses.init_pair(0, 255, 0) # id 0, white text, black background
    curses.init_pair(1, 0, 255) # id 1, black text, white background

    index_selected_theme = 0
    index_selected_answer = 0

    number_of_questions = len(fake_questions)
    current_question = 0
    number_of_questions_by_line = 2

    state = 1

    while c != ord('q'):
        stdscr.clear()

        maxY, maxX = stdscr.getmaxyx()

        if c == 10: # Enter
            if number_of_questions == 0:
                break
            elif (state == 2 and current_question < (number_of_questions - 1)):
                current_question += 1
                index_selected_answer = 0
            else:
              state += 1
        if state > 3:
            break

        if (maxY > (5 * math.ceil(number_of_artists / number_of_themes_by_line)) and maxX > max_line_length + number_of_themes_by_line):
            if state == 1:
                index_selected_theme = get_index_selected_item(index_selected_theme, c, number_of_artists, number_of_themes_by_line)
                display_items(stdscr, artists, maxX, maxY, number_of_themes_by_line, index_selected_theme)
            elif state == 2:
                data = fake_questions[current_question]
                question = data["question"]
                validAnswer = data["validAnswer"]
                wrongAnswers = data["wrongAnswers"]
                answers = [validAnswer] + wrongAnswers

                max_length = max(len(answer) for answer in answers)
                answers = [f"{answer.center(max_length)}" for answer in answers] # fill of spaces to have the same length

                # display_questions(stdscr, maxX, maxY, artists[index_selected_theme])
                index_selected_answer = get_index_selected_item(index_selected_answer, c, len(answers), number_of_questions_by_line)
                display_items(stdscr, answers, maxX, maxY, number_of_questions_by_line, index_selected_answer)
            elif state == 3:
                pass
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
