# Variables
string = ["str", "s", "string"]
integer = ["int", "i", "integer"]
flaot = ["flt", "f", "float"]
boolean = ["bln", "b", "bool", "boolean"]

# ->Input
value = input("Skriv noe her:\n")
dataType = input("Hvilken datatype vil du ha det i?\n").lower()

# ->Templates
inputTemplate = f'Hvilken datatype vil du ha verdien din i?'
errorTemplate = f'Verdien kan ikke konverteres til "{dataType}" datatype.'
nanTemplate = f'"{dataType}" er ikke en valid datatype.'

# Calculation
while True:
    if dataType in string:
        try:
            value = str(value)
            break
        except:
            dataType = input(f'{errorTemplate}\n{inputTemplate}\n').lower()

    elif dataType in integer:
        try:
            value = int(value)
            break
        except:
            dataType = input(f'{errorTemplate}\n{inputTemplate}\n').lower()
    elif dataType in flaot:
        try:
            value = float(value)
            break
        except:
            dataType = input(f'{errorTemplate}\n{inputTemplate}\n').lower()
    elif dataType in boolean:
        try:
            value = bool(value)
            break
        except:
            dataType = input(f'{errorTemplate}\n{inputTemplate}\n').lower()
    else:
        dataType = input(f'{nanTemplate}\n{inputTemplate}\n').lower()

# Output
print(f'Datatypen din er ferdig konvertert! Nå ser de ut sånn:\n{value}')