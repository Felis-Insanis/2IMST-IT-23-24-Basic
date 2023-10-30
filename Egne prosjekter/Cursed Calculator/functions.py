import curses

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
    while index < len(equasionList): # ganger og deler
        screen.addstr(str(equasionList[index])) # debug
        if equasionList[index] == '/':
            equasionList[index] = equasionList[index-1] / equasionList[index+1]
            del equasionList[index+1], equasionList[index-1]
            index += -2
        elif equasionList[index] == '*':
            equasionList[index] = equasionList[index-1] * equasionList[index+1]
            del equasionList[index+1], equasionList[index-1]
            index += -2
        index += 1

    index = 0
    while index < len(equasionList): # addisjon og subtraksjon
        screen.addstr(str(equasionList[index])) # debug
        if equasionList[index] == '+':
            equasionList[index] = equasionList[index-1] + equasionList[index+1]
            del equasionList[index+1], equasionList[index-1]
            index += -2
        elif equasionList[index] == '-':
            equasionList[index] = equasionList[index-1] - equasionList[index+1]
            del equasionList[index+1], equasionList[index-1]
            index += -2
        index += 1
    return equasionList[0]

def removeParenctheses(equasionList: list, screen = curses.initscr()):
    screen.move(14, 0)
    index = 0
    nrParenctheses = 0
    while '(' in equasionList:
        while index < len(equasionList):
            screen.addstr(str(equasionList[index]))
            screen.getch()
            if equasionList[index] == '(':
                left = index
                break
            index += 1
        while index < len(equasionList):
            screen.addstr(str(equasionList[index]))
            screen.getch()
            if equasionList[index] == '(':
                nrParenctheses += 1
            elif equasionList[index] == ')':
                nrParenctheses -= 1
            if nrParenctheses == 0:
                right = index-len(equasionList)
                break
            index += 1

        separated = equasionList[left+1:]
        equasionList = equasionList[:left]
        equasionList.append(separated[right+1:])
        separated = separated[:right]

        screen.addstr(10, 10, str(equasionList))
        
        screen.addstr(str(separated))

        while '(' in separated:
            separated = removeParenctheses(separated, screen)
        
        result = calculation(separated)
        
        equasionList.insert(left, result)

    return equasionList