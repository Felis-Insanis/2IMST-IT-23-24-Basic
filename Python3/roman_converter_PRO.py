'''
Roman numbers is a number-system used by the ancient Romans.
You can still see them today, maybe in tattoos and on watches.
An example is the number 26, which translates to the
Roman number of XXVI.
'''

# TASK

'''
Make a num_to_roman transformer, that takes in an integer
and prints the transformed value.

Roman values:
1 = I, IV = 4, 5 = V, IX = 9, 10 = X, XL = 40, L = 50, XC = 90, C = 100, CD = 400, D = 500, CM = 9000, M = 1000
'''
import curses # for visuals

decimal = 0
'''the raw user input in integer form, if the input actually is decimal'''

symbols = {1000: "M",900: "CM",500: "D",400: "CD",100: "C",90: "XC",50: "L",40: "XL",10: "X",9: "IX",5: "V",4: "IV",1: "I",}
'''a dictionary for Roman numeric symbols of decimal values'''

def decimalToRoman(decimal, screen):
    '''converts decimal values to Roman numerals'''
    if -1 < decimal < 3999:
        screen.addstr(0, 0, '')
        roman = ''
        '''the roman number'''
        for value, symbol in symbols.items(): # fills out the roman number, while depleting the decimal number
            while decimal >= value:
                roman += symbol
                decimal -= value

        if roman == '': # assigns the "nothing" symbol to roman
            roman = 'Ø'

        screen.addstr(0, 0, roman)
    else:
        screen.addstr(0, 0, 'Calculo refuses to convert numbers lower than 0 or higher than 3999.')

def romanToDecimal(roman, screen) -> str:
    '''converts Roman numbers to decimal values''' # utvikling senere
    pass

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

stdscr = curses.initscr()
'''the standard screen, on which everything is based'''

curses.noecho()
'''keypresses won't be echoed on screen this way'''

maxY, maxX = stdscr.getmaxyx()
'''the maximum coordinate on the terminal window, for referential purposes'''

inputBox = stdscr.subwin(3, 14, int(maxY/2)-2, int(maxX/2)-8)
'''a box around the actual input area'''
inputBox.box()

inputArea = inputBox.derwin(1, 12, 1, 2)
'''the area where input is done'''

stdscr.refresh() # refreshes the window alongside every child window it has

number = keyboardInput(inputArea)
'''the raw user input, potentially roman, potentialy arabic decimal'''

try:
    decimal = int(number)
except:
    romanToDecimal(number, stdscr) # gjør ingenting akkurat nå
else:
    decimalToRoman(decimal, stdscr) # runs the roman -> arabic decimal conversion

stdscr.getch() # stops the program from going on until user presses a key

curses.endwin() # end of program, restores terminal