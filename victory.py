import random


def play_victory_game():
    day_dict = {'1': 'первое', '3': 'третье', '9': 'девятое', '13': 'тренадцатое', '14': 'четырнадцатое',
                '18': 'восемьнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '23': 'двадцать третье',
                '30': 'тридцатое'}

    month_dict = {'01': 'января', '03': 'марта', '04': 'апреля', '08': 'августа', '09': 'сентября', '10': 'октября',
                  '12': 'декабря', }

    popular_peoples = {'Альберт Эйнштейн': '14.03.1879', 'Л.Н. Толстой': '09.09.1828', 'С.А. Есенин': '03.10.1895',
                       'И.В. Сталин': '18.12.1878', 'Макс Планк': '23.04.1858', 'Ольга Бузова': '20.01.1986',
                       'Ким Кардашян': '21.10.1980', 'Тейлор Свифт': '13.12.1989', 'Мила Кунис': '14.08.1983',
                       'Камерон Диас': '30.08.1972'}

    random_peoples = random.sample(list(popular_peoples.keys()), 5)

    repeat = 'да'

    while repeat == 'да':
        right_answers = 0

        for i in random_peoples:
            answer = input(f'Веедите дату рождения {i}: ')
            if answer == popular_peoples[i]:
                print('Верно')
                right_answers += 1
            else:
                right_date = popular_peoples[i].split('.')
                print(
                    f'Неверно, правильный ответ: {day_dict[right_date[0]]} {month_dict[right_date[1]]} {right_date[2]} года')

        total_answers = len(random_peoples)
        wrong_answers = total_answers - right_answers

        print()
        print('количество правильных ответов:', right_answers)
        print('количество ошибок:', wrong_answers)

        repeat = input('хотите начать игру сначала? да/нет: ')
