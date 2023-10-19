allowance = float(input('Hvor mye penger har du?\n'))

if allowance < 20:
    print('Du kan ikke kjøpe noe med så lite. Kom tilbake senere!')
elif 20 <= allowance < 30:
    print('Du kan kjøpe 1 brus med pengene dine.')
elif 30 <= allowance < 50:
    print('Du kan kjøpe enten 1 brus eller 1 godteri.')
elif 50 <= allowance:
    print('Du kan kjøpe både brus og godteri samtidlig.')