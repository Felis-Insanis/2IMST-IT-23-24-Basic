a = 0

for numbers in range(10, 20):
    a += numbers
    if a >= 50:
        break
print(f'Sluttresultatet er: {a}')