columns = [1, 2, 3]
for rows in range(3):
    print(f'{columns[0] + rows}      {columns[1] + rows}      {columns[2] + rows}')
    for column in range(len(columns)):
        columns[column] += 2