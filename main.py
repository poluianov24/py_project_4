print('''\033[33mОберіть фігуру яку бажаєте відобразити серед доступних:
\033[34m
*  *  *  *  *       *                   *  *  *  *  *                           *  *  *  *  *
   *  *  *  *       *  *                   *  *  *                                 *  *  *   
      *  *  *       *  *  *                   *                   *                   *      
         *  *       *  *  *  *                                 *  *  *             *  *  *   
            *       *  *  *  *  *                           *  *  *  *  *       *  *  *  *  *
      \033[36m1.                  2.                  3.                  4.                  5.
\033[34m
*           *       *                               *       *  *  *  *  *                   *
*  *     *  *       *  *                         *  *       *  *  *  *                   *  *
*  *  *  *  *       *  *  *                   *  *  *       *  *  *                   *  *  *
*  *     *  *       *  *                         *  *       *  *                   *  *  *  *
*           *       *                               *       *                   *  *  *  *  *
      \033[36m6.                  7.                  8.                  9.                  10.''')
while True:
    figure = input('\033[33mДля вибору фігури яку необхідно відобразити введіть її номер (для виходу введіть \'0\'): ')
    if figure.isdigit():
        number = int(figure)
        if number == 0:
            print('\033[31mДо зустрічі')
            break
        elif number == 1:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input('\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if i <= j:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 2:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if i >= j:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 3:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if i + j >= x:
                                print(end='   ')
                            elif i <= j:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 4:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if i + j < x - 1:
                                print(end='   ')
                            elif i >= j:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 5:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if i <= j and i + j < x:
                                print(s, end='  ')
                            elif i >= j and i + j >= x - 1:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 6:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
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
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 7:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if j > i:
                                print(end='   ')
                            elif i + j < x:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 8:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if j < i:
                                print(end='   ')
                            elif i + j >= x - 1:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 9:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if j + i < x:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
        elif number == 10:
            print(f'\033[34mВи обрали фігуру №: {number}')
            s = input('\033[33mВведіть один символ для заповнення фігури: ')
            while True:
                x = input(
                    '\033[33mВведіть максимальну довжину сторони фігури (для вибору іншої фігури введіть \'0\'): ')
                if x.isdigit():
                    x = int(x)
                    if x == 0:
                        break
                    print('\033[35m')
                    i = j = 0
                    while i < x:
                        while j < x:
                            if j + i >= x - 1:
                                print(s, end='  ')
                            else:
                                print(end='   ')
                            j += 1
                        print()
                        j = 0
                        i += 1
                else:
                    print('\033[31mНекоректно вказана довжина. Введіть максимальну довжину сторони фігури яка > 0.')
    else:
        print('\033[31mНекоректно обрана фігура. Оберіть фігуру серед доступних (від 1 до 10).')
