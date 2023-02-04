def start_bank_account():
    wallet = 0
    history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            wallet += int(input('На сколько пополнить счет? '))
            print('Сумма на счете', wallet)
        elif choice == '2':
            price = int(input('Введите сумму покупки: '))
            if price > wallet:
                print('Недостаточно средств для покупки!')
            else:
                goods_name = input('Введите название покупки: ')
                wallet -= price
                history.append(f'{goods_name} - {price}')
        elif choice == '3':
            for i in history:
                print(i)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
