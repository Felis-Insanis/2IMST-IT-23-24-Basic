from dunGen import *
from gobbo import *

length = int(input('How long should the dungeon be?\n'))
width = int(input('How wide should the dungeon be?\n'))

dungeon = generateNewDungeon(length, width)
dungeon = generateWalls(dungeon, length, width)
print('Dungeon map:')
for i in range(len(dungeon)):
    print(dungeon[i])

loot, ruins = greedyGoblin(dungeon, length, width)

print(f'The goblin escaped with {loot} coins!')

print('What remains:')
for i in range(len(ruins)):
    print(ruins[i])