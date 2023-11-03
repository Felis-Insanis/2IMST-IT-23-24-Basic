import random
def generateNewDungeon(rows, columns):
    newDungeon = []
    for row in range(rows):
        newDungeon.append([])
        for column in range(columns):
            newDungeon[row].append(str(random.randint(0, 9)))
    return newDungeon

def generateWalls(dungeon, rows, columns):
    for y in range(rows):
        for x in range(columns):
            try:
                if dungeon[y-1][x+1] != '\u2588' and  y != rows-1 and x != columns-1 and [y, x] != [0, 0]:
                    if random.randint(1, 3) == 1:
                        dungeon[y][x] = '\u2588'
            except:
                print(f'Row {y+1} complete!')
    return dungeon