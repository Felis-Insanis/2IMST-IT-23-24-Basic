import curses
from curses import wrapper

def keyboardInput(screen = curses.initscr()):
    '''responsible for being able to type'''
    rawInput = ''
    while True:
        y, x = screen.getyx()
        character = screen.getkey()
        if character == "\n":
            break
        elif character == "\x7F":
            try:
                screen.addstr("\b ")
                screen.addstr('\b')
                screen.refresh()
            except:
                pass
            rawInput = rawInput[:-1]
        else:
            screen.addstr(character)
            rawInput += character
    return rawInput

def main(stdscr = curses.initscr()):

    maxY, maxX = stdscr.getmaxyx()

    inscr = stdscr.subwin(10, 100, maxY-15, 5)
    
    # Keyboard input
    rawInput = keyboardInput(inscr)
    stdscr.addstr(rawInput)
    stdscr.getch()


wrapper(main)