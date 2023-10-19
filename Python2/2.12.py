tekst = 'Uten mat og drikke, duger helten ikke.'
vokaler = 'aeiouyæøå'

print('Vokalene:')
for character in tekst: # printer ut vokalene
    if character.lower() in vokaler:
        print(f'\t- {character.lower()}')
    else:
        pass

print('\nKonsonantene:')
for character in tekst: # printer ut konsonantene
    if character.lower() not in vokaler+' '+'.'+',':
        print(f'\t- {character.lower()}')
    else:
        pass