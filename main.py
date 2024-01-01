try:
    s = input('\033[33mВведіть символ для заповнення фігури: ')
    x = int(input('Введіть довжину сторони квадратап: '))
    i = j = 0
    print('\033[35m')
    while i < x:
        while j < x:
            if i < j and i + j < x - 1:
                print(end='   ')
            elif i > j and i + j >= x:
                print(end='   ')
            else:
                print(s, end='  ')
            j += 1
        print()
        j = 0
        i += 1
except Exception as e:
    print(e)