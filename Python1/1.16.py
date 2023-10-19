carsSold = int(input('Hvor mange biler har du solgt?\n'))

bruttoStonks = carsSold*500
if carsSold > 70:
    nettoStonks = bruttoStonks+5000
    print(f'Gratulerer! Du har solgt flere enn 70 biler! Du får 5000kr bonus. Du får {nettoStonks}kr lønn totalt.')
else:
    nettoStonks = bruttoStonks
    print(f'Du har ikke solgt flere enn 70 biler, så får du ikke bonus. Du får {nettoStonks}kr lønn totalt.')