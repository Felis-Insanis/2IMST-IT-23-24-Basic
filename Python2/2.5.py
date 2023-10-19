answer = ''
isExit = False

while isExit == False:
    answer = input("Write 'Exit' to exit the program. ")

    if answer == 'Exit':
        isExit = True
        print(f"'{answer}'ing...")
    else:
        print(answer)
        print(f"\n'{answer}'isn't the same as 'Exit'.")