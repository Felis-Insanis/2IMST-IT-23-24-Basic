def greedyGoblin(dungeon: list, maxY: int, maxX: int):
    treasury = dungeon
    x = 0
    y = 0
    treasureHeld = int(treasury[y][x])
    treasury[y][x] = ' '
    treasureToEast = 0
    treasureToSouth = 0
    step = 0
    print(f'Initial treasure: {treasureHeld} coins')

    for i in range(maxX+maxY-2):
        step += 1
        try:
            treasureToEast  = int(treasury[y][x+1])
        except:
            treasureToEast = -1
        try:
            treasureToSouth = int(treasury[y+1][x])
        except:
            treasureToSouth = -1

        if   treasureToEast >= treasureToSouth:
            x += 1
            treasureHeld += int(treasury[y][x])
            print(f'Round {step}\nCoins picked up: {treasury[y][x]}\nCurrent treasure: {treasureHeld} coins\n')
            treasury[y][x] = ' '
        elif treasureToEast < treasureToSouth:
            y += 1
            treasureHeld += int(treasury[y][x])
            print(f'Round {step}\nCoins picked up: {treasury[y][x]}\nCurrent treasure: {treasureHeld} coins\n')
            treasury[y][x] = ' '

    return treasureHeld, treasury