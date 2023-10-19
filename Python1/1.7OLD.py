# Variables
y = ['y', 'yes', '+', 'j', 'ja']
n = ['n', 'nei', '-', 'no']
yn = ''

# ->Input
number1, number2 = input('Skriv inn to tall du vil legge sammen:\n').strip('asd')

# Calculation
number1 = float(number1) + float(number2)

while True:
    yn = input('Vil du fortsette?').lower()
    if yn in y:
        number2 = float(input('Skriv inn et tall:\n'))
        number1 = float(number1) + float(number2)
    elif yn in n:
        break
    else:
        print('Du skrev noe galt. Prøv igjen!')

# Output
print('Sluttresultaten din er ', number1)