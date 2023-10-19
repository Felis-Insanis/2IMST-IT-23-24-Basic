# Variables
y = ['y', 'yes', '+', 'j', 'ja']
n = ['n', 'nei', '-', 'no']
yn = ''

# ->Input
inn = input('Skriv inn to tall du vil legge sammen:\n').split()

number1 = float(inn[0])
number2 = float(inn[1])

# Calculation
number1 = number1 + number2

while True:
    yn = input(f'Nå står du på {number1}.\nVil du fortsette? ').lower()
    if yn in y:
        number2 = float(input('Skriv inn et tall:\n'))
        number1 = float(number1) + float(number2)
    elif yn in n:
        break
    else:
        print('Du skrev noe galt. Prøv igjen!')

# Output
print('Sluttresultaten din er ', number1)