def display_questions(stdscr, maxX: int, maxY: int, theme: str):
  stdscr.addstr(maxY // 2, maxX // 2 - len(theme) // 2, theme)
