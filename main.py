import os
import shutil
import sys
from victory import play_victory_game
from bank_account import start_bank_account
while True:
    print('*' * 20)
    print('1. создать папку')
    print('2. удалить(файл / папку)')
    print('3. копировать(файл / папку)')
    print('4. просмотр содержимого рабочей директории;)')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории(*необязательный пункт)')
    print('12. выход')
    print()

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        folder_name = input('Введите название папки для создания: ')
        if os.path.exists(folder_name):
            print('Папка с таким именем уже существует')
        else:
            os.mkdir(folder_name)

    if choice == '2':
        path = input('Введите название папки/файла для удаления: ')
        if not os.path.exists(path):
            print('Папка/файл с таким именем не существует')
        elif os.path.isfile(path):
            os.remove(path)
        else:
            os.rmdir(path)

    if choice == '3':
        file_names = input('Введите "название папки/файла, новое название папки/файла" для копирования: ').split(', ')
        if not os.path.exists(file_names[0]):
            print('папки/файла с таким именем не существует')
        elif os.path.isfile(file_names[0]):
            shutil.copy(file_names[0], file_names[1])
        else:
            shutil.copytree(file_names[0], file_names[1])

    if choice == '4':
        dir_list = os.listdir(os.getcwd())
        print('Список содержимого:')
        for i in dir_list:
            print(i, end=', ')
        print()

    if choice == '5':
        dir_list = os.listdir(os.getcwd())
        print('Список папок:')
        for i in dir_list:
            if os.path.isdir(i):
                print(i, end=', ')
        print()

    if choice == '6':
        dir_list = os.listdir(os.getcwd())
        print('Список файлов:')
        for i in dir_list:
            if os.path.isfile(i):
                print(i, end=', ')
        print()

    if choice == '7':
        print(sys.platform)

    if choice == '8':
        print('Copyright Dmitry')

    if choice == '9':
        play_victory_game()

    if choice == '10':
        start_bank_account()

    if choice == '11':
        break

print()
