import json
import os
import shutil
import sys
from victory import play_victory_game
from bank_account import start_bank_account


def get_file_names_list(func):
    files_list = os.listdir(os.getcwd())
    return list(filter(func, files_list))


if __name__ == '__main__':
    while True:
        print('*' * 20)
        print('1. создать папку')
        print('2. удалить(файл / папку)')
        print('3. копировать(файл / папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. сохранить содержимое рабочей директории в файл')
        print('6. посмотреть только папки')
        print('7. посмотреть только файлы')
        print('8. просмотр информации об операционной системе')
        print('9. создатель программы')
        print('10. играть в викторину')
        print('11. мой банковский счет')
        print('12. смена рабочей директории(*необязательный пункт)')
        print('13. выход')
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
            file_names = input('Введите "название папки/файла, новое название папки/файла" для копирования: ').split(
                ', ')
            if not os.path.exists(file_names[0]):
                print('папки/файла с таким именем не существует')
            elif os.path.isfile(file_names[0]):
                shutil.copy(file_names[0], file_names[1])
            else:
                shutil.copytree(file_names[0], file_names[1])

        if choice == '4':
            dir_list = get_file_names_list(lambda d: d)
            print('Список содержимого:')
            for i in dir_list:
                print(i, end=', ')
            print()

        if choice == '5':
            files = get_file_names_list(lambda d: os.path.isfile(d))
            folders = get_file_names_list(lambda d: os.path.isdir(d))
            with open('listdir.txt', 'w', encoding='utf-8') as f:
                json.dump({'files': files}, f)
                f.write('\n')
                json.dump({'folders': folders}, f)

        if choice == '6':
            print('Список папок:')
            folders = get_file_names_list(lambda d: os.path.isdir(d))
            for i in dir_list:
                if os.path.isdir(i):
                    print(i, end=', ')
            print()

        if choice == '7':
            print('Список файлов:')
            files = get_file_names_list(lambda d: os.path.isfile(d))
            for i in files:
                print(i, end=', ')
            print()

        if choice == '8':
            print(sys.platform)

        if choice == '9':
            print('Copyright Dmitry')

        if choice == '10':
            play_victory_game()

        if choice == '11':
            start_bank_account()

        if choice == '12':
            break

    print()
