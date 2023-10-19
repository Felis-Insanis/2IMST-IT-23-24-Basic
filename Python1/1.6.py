# Variables
# ->Input
timelønn, timerJobbet = input('''Hvor mange kroner får du per time og hvor mange timer jobber du i et ike?\n''').split(', ')
skatt = float(input("Hvor stor er skatten din?\n").strip("%"))

# Calculation
bruttolønn = 4 * float(timelønn) * float(timerJobbet)
skattBetalt = bruttolønn * (skatt / 100)
nettolønn = bruttolønn - skattBetalt

# Output
print("\nDu jobber", timerJobbet, "timer i uka og får", timelønn, "kroner hver time, så får du cirka", bruttolønn, "kroner brutto hver måned.\nDu skatter", str(skatt) + "%", "av lønnen din, som tilpasser til", skattBetalt, "kroner betalt.\nTil slutt får du", nettolønn, "kroner av lønnen din.")