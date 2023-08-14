# статический метод посмотреть теорию
# raise для описания своих ошибок
# while True:
#     try:
#         login = input('Введите логин: ')
#         if len(login) <= 3:
#             raise Exception('Введен короткий логин повторите ввод')
#         if len(login) >= 30:
#             raise Exception('Введен длинный логин повторите ввод')
#
#         break
#     except Exception as error:
#         print(f'Ошибка {error}')
# try:
#     password = input('Введите пароль: ')
#     if len(password) >= 8:
#         raise Exception('Введен не верный пароль повторите ввод')
# except Exception as error:
#     print(error)
# print(f'Вы ввели логин такой: {login} и пароль: {password}')

import os

programers = []
with open('text.txt', 'r', encoding="utf-8") as textFile:
    someProgramers = textFile.readlines()
    programers = [programer.rstrip('\n') for programer in someProgramers]

while True:
    try:
        print('0 - Выход')
        print('1 - Количество программистов на проекте')
        print('2 - Добавить программиста на проект')
        print('3 - Убрать программиста с проекта')
        programers.sort()
        option = input('Выберите действие из списка: ')

        if option == '0':
            with open('text.txt', 'w', encoding="utf-8") as textFile:
                textFile.writelines([car + '\n' for car in programers])

            break

        elif option == '1':
            print('Количество программистов на проекте')
            for programer in programers:
                print(' - ' + programer)

        elif option == '2':
            programer = input('Введите ФИО программиста для добавления на проект: ')
            raise Exception('Введены символы необходим цифровой выбор действия')
            # if programer.isalpha():
            programers.append(programer)

            #     print(f'Программист {programer} добавлен на проект ')
            # else:
            #     print('Ошибка введена не корректная фамилия повторите ввод')

        elif option == '3':
            print(programers)
            programer = int(input('Выберите программиста для перевода на др. проект по индексу: '))
            programers.pop(programer)
            print(f'Программисты {programers} остались на проект а программист {programer} переведен на другой проект')

    except Exception as error:
        print(f'Ошибка {error}')
    #
    # os.system('Ожидание')
    # os.system('cls')

print('Пока')
