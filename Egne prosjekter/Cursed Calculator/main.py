# imports
import curses
from curses import wrapper
from functions import *

stdscr = curses.initscr()
curses.noecho()

inputWindow = stdscr.subwin(1, 50, 0, 0)
# rawEquasion = keyboardInput(inputWindow).strip()
# equasion = convertToList(rawEquasion)
equasion = [2, '*','(', 1, '+', 2, '*', '(', 1, '+', 2, ')', '+', 2, '*', '(', 3, '+', 2, ')', ')']

stdscr.addstr(2, 1, f'= {str(equasion)}')
if '(' in equasion:
    equasion = removeParenctheses(equasion, stdscr)
result = calculation(equasion, stdscr)
stdscr.addstr(2, 1, f'= {result}')

stdscr.getch()

curses.endwin()