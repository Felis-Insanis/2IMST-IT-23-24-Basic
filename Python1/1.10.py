# Variables
# ->Input
nr1 = float(input('Type in the first number:\n'))
nr2 = float(input('Type in the second number:\n'))

# Output
if nr1 < nr2:
    print(f'{nr1} er mindre enn {nr2}.')
elif nr1 == nr2:
    print(f'{nr1} er lik {nr2}.')
elif nr1 > nr2:
    print(f'{nr1} er større enn {nr2}.')
else:
    print('Error: Something didn\'t work out.')