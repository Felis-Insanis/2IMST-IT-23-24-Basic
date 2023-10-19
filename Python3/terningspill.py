import random # randomising through Random lib.

def castDice(diceAmount: int, diceSides: int) -> int:
    '''simulates throwing the given number of the given type of dice'''
    result: list = []
    for dice in range(diceAmount):
        result.append(random.randint(1, diceSides))

def yesOrNo(message:str) -> bool:
    success = input(message).lower
    while success not in ['y', 'n', 'yes', 'no']:
        success = input('Invalid option.\n' + message)
    if success in ['y', 'yes']:
        return True
    else:
        return False

def startGame() -> str:
    '''initiates game'''
    sidedDice = [4, 6, 8, 10, 12, 20]
    typeDice: int = 0
    players: dict = {}

    nrPlayers = int(input('How many players are there?\n'))

    for player in range(1, nrPlayers):
        players += {f'Player{player}': 0}

    if yesOrNo('Do you want the option of different dice sets every round?') == True:
        maxScorePerTurn = int(input('What do you want the highest possible throw to be?'))
        print('\nTHE GAME STARTS\n')
        for player in range(1, nrPlayers):
            print(f'Player {player}\'s turn!')
            
    else:
        nrDice = int(input('How many dice should be rolled?\n'))
        while typeDice not in range(1, 5):
            typeDice = int(input('Which dice should be rolled?\n1: d4\n2: d6\n3: d8\n4: d10\n5: d12\n5: d20'))

startGame()