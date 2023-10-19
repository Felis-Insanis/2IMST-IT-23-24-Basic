# Modulo (%) kalkuleres hvor mye er resten i en deling før decimaler.
# f.eks: 10%3 blir 1, siden 9 er det siste tall før 10 som kan deles med 3 for å få heltall, og 10-9=1
# Så blir 17%3 2: 15 er det siste tall før 17 som kal deles med 3 for å få heltall, og 17-15=2

numbers = [10, 17, 17, 17]
modulos = [3, 2, 3, 6]

for i in range(len(numbers)):
    print(f'Moduloen av {numbers[i]}/{modulos[i]} er {numbers[i]%modulos[i]}.')