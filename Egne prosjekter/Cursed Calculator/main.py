# imports
import curses
import curses.textpad
from curses import wrapper

# definitions
def keyboardInput(screen):
    '''responsible for being able to type'''
    rawInput = ''
    '''the input'''
    while True:
        character = screen.getkey() # records keypress
        if character == "\n": # stopping the recording process
            return rawInput
        elif character == "\x7F": # backspace (suprisingly difficult)
                rawInput = rawInput[:-1]
                screen.addstr('\b ')
                screen.addstr('\b')
                screen.refresh()
        else: # records keypresses and puts them on screen
            rawInput += character
            screen.addstr(character)
            character = ''

def convertToList(string):
    charlist = []
    for character in string: # algorytmen til å koble sammen sammenhengende tall
        try: # viser hvis karakteren i strengen er et tall eller ikke
            float(character)
            isCurrentNumber = True
        except:
            isCurrentNumber = False
        try: # viser hvis previøs karakteren i streng er et tall eller ikke
            float(charlist[-1])
            isNumber = True
        except:
            isNumber = False

        if isNumber == True and isCurrentNumber == True:
            charlist[-1] += character
        elif character == ' ':
            pass
        else:
            charlist.append(character)

    for item in range(len(charlist)): # gjør at alle tall strenger blir til float i listen
        try:
            charlist[item] = float(charlist[item])
        except:
            pass
    return charlist

def calculation(equasionList, screen = curses.initscr()): # gjør kalkulasjonene i orden
    screen.move(12, 0) # debug
    index = 0
    equ = equasionList
    while index < len(equ): # ganger og deler
        screen.addstr(str(equ[index])) # debug
        if equ[index] == '/':
            equ[index] = equ[index-1] / equ[index+1]
            del equ[index+1], equ[index-1]
            index += -2
        elif equ[index] == '*':
            equ[index] = equ[index-1] * equ[index+1]
            del equ[index+1], equ[index-1]
            index += -2
        index += 1

    index = 0
    while index < len(equ): # addisjon og subtraksjon
        screen.addstr(str(equ[index])) # debug
        if equ[index] == '+':
            equ[index] = equ[index-1] + equ[index+1]
            del equ[index+1], equ[index-1]
            index += -2
        elif equ[index] == '-':
            equ[index] = equ[index-1] - equ[index+1]
            del equ[index+1], equ[index-1]
            index += -2
        index += 1
    return equ[0]

def removeParenctheses(equasionList, screen = curses.initscr()):
    screen.move(14, 0)
    index = 0
    nrParenctheses = 0
    equ = equasionList
    while index < len(equ):
        screen.addstr(str(equ[index]))
        screen.getch()
        if equ[index] == '(':
            left = index
            break
        index += 1
    while index < len(equ):
        screen.addstr(str(equ[index]))
        screen.getch()
        if equ[index] == '(':
            nrParenctheses += 1
        elif equ[index] == ')':
            nrParenctheses -= 1
        if nrParenctheses == 0:
            right = index-len(equ)
            break
        index += 1
    separated = equ[left+1:]
    separated = separated[:right]
    screen.addstr(str(separated))

def main(stdscr = curses.initscr()): # smaling av alt oppover + visuelle ting
    inputWindow = stdscr.subwin(1, 50, 0, 0)
    rawEquasion = keyboardInput(inputWindow).strip()
    equasion = convertToList(rawEquasion)

    stdscr.addstr(2, 1, f'= {str(equasion)}')
    if '(' in equasion:
        removeParenctheses(equasion, stdscr)
    else:
        result = calculation(equasion, stdscr)
        stdscr.addstr(2, 1, f'= {result}')

    stdscr.getch()

wrapper(main) # kjøres koden