import os.path
import json


def manage_wallet(amount, func):
    return func(amount)


def start_bank_account():
    wallet = 0
    history = []
    if os.path.exists('bank_account.json'):
        with open('bank_account.json', 'r') as f:
            account_data = json.load(f)
            wallet = int(account_data[0])
            history = account_data[1]

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            amount = int(input('На сколько пополнить счет? '))
            wallet = manage_wallet(wallet, lambda x: x + amount)
            print('Сумма на счете', wallet)
        elif choice == '2':
            amount = int(input('Введите сумму покупки: '))
            if amount > wallet:
                print('Недостаточно средств для покупки!')
            else:
                goods_name = input('Введите название покупки: ')
                wallet = manage_wallet(wallet, lambda x: x - amount)
                history.append((goods_name, amount))
        elif choice == '3':
            for i in history:
                print(i)
        elif choice == '4':
            with open('bank_account.json', 'w') as f:
                json.dump([wallet, history], f)
            return wallet
        else:
            print('Неверный пункт меню')
