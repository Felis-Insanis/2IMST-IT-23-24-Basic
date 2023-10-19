# Imports
import random

# Variables and Lists
nuumbeersssssssssssss = []
maximum = 0.0
minimum = 0.0
absolute = 0.0
round

# Generating list
for i in range(3):
    nuumbeersssssssssssss.append(random.uniform(0.0, 100.0))
    nuumbeersssssssssssss.append(random.uniform(0.0, -100.0))

# Finding maximum value
for i in range(len(nuumbeersssssssssssss)):
    if maximum <= nuumbeersssssssssssss[i]:
        maximum = nuumbeersssssssssssss[i]
    else:
        pass

altMaximum = max(nuumbeersssssssssssss)

# Finding minimum value
for i in range(len(nuumbeersssssssssssss)):
    if minimum >= nuumbeersssssssssssss[i]:
        minimum = nuumbeersssssssssssss[i]
    else:
        pass

altMinimum = min(nuumbeersssssssssssss)

# Finding an absolute value
index1 = random.randint(0, 5)
absolute = nuumbeersssssssssssss[index1]

if absolute < 0:
    absolute = absolute * -1

altAbsolute = abs(nuumbeersssssssssssss[index1])

# Roundung a number
index2 = random.randint(0, 5)
decimals = random.randint(-2, 3)
rounded = round(nuumbeersssssssssssss[index2], decimals)
# I couldn't be bothered to make my own algorythm for this.

# Output
print(f'This analysis is based on the following list: {nuumbeersssssssssssss}.\nThe highest value in the list is {maximum} ({altMaximum} with the built in method).\nThe lowest value in the list is {minimum} ({altMinimum} with the built in method).\nThe absolute value of the {index1 +1}th item on the list is {absolute} ({altAbsolute} with the built in method).\nThe {index2}th item on the list rounded down to {decimals} decimals equals {rounded}.')