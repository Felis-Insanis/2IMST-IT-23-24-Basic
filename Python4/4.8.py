import random
numList = []

for i in range(5):
    numList.append(random.randint(-1000000, 1000000))

print(numList)

def maxIntOfList(list):
    print('Finding the maximum:')
    storage = list[0]
    for i in range(len(list)-1):
        print(f'Number 1: {list[i]}\nNumber 2: {list[i+1]}\nStorage: {storage}\n')
        if list[i] > list[i+1]:
            if list[i] > storage:
                storage = list[i]
        elif list[i] < list[i+1]:
            if list[i+1] > storage:
                storage = list[i+1]
    print(f'The maximum number in this list is is: {storage}\n\n')
    return storage

def minIntOfList(list):
    print('Finding the minimum:')
    storage = list[0]
    for i in range(len(list)-1):
        print(f'Number 1: {list[i]}\nNumber 2: {list[i+1]}\nStorage: {storage}\n')
        if list[i] < list[i+1]:
            if list[i] < storage:
                storage = list[i+1]
        elif list[i] > list[i+1]:
            if list[i+1] < storage:
                storage = list[i]
    print(f'The minimum number in this list is is: {storage}\n\n')
    return storage

maxInt = maxIntOfList(numList)
minInt = minIntOfList(numList)

print(f'The highest number in the list is:\n{maxInt}\nThe lowest number in the list is:\n{minInt}')