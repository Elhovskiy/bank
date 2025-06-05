import argparse
from models.customer import Customer

def command_interface(command, bank, auth):
    args = command.strip().split()
    if not args:
        return
    cmd = args[0]

    if cmd == 'login':
        if len(args) < 3:
            print("⚠️ Использование: login <name> <password>")
            return
        try:
            auth.authentication(args[1], args[2])
        except Exception as e:
            print(f"❌ Ошибка входа: {e}")
        bank.load_account()
    elif cmd == 'regist':
        if len(args) < 3:
            print("⚠️ Использование: regist <name> <password>")
            return
        try:
            auth.registration(args[1], args[2])
        except Exception as e:
            print(f"❌ Ошибка входа: {e}")
    elif cmd == 'add_ac':
        if not auth.checking_user_authentication():
            return
        try:
            bank.add_account_bd()
        except Exception as e:
            print(f"❌ Ошибка добавлении счета: {e}")

    elif cmd == 'list_ac':
        if not auth.checking_user_authentication():
            return
        bank.list_of_account()

    elif cmd == 'deposit':
        if not auth.checking_user_authentication():
            return
        account = bank.accounts.get(args[1])
        if not account:
            print("❌ Счет не найден.")
            return
        if account.owner != auth.current_user.name:
            print("❌ Вы не владелец этого счета.")
            return
        account.deposit(int(args[2]))

    elif cmd == 'withdraw':
        if not auth.checking_user_authentication():
            return
        print(bank.accounts.get(args[1]))
        account = bank.accounts.get(args[1])
        if not account:
            print("❌ Счет не найден.")
            return
        if account.owner != auth.current_user.name:
            print("❌ Вы не владелец этого счета.")
            return
        account.withdraw(int(args[2]))

    elif cmd == 'transfer':
        if not auth.checking_user_authentication():
            return
        from_account_id = args[1]
        to_account_id = args[2]
        amount = int(args[3])

        from_account = bank.accounts.get(from_account_id)
        if not from_account or from_account.owner != auth.current_user.name:
            print("❌ Нельзя переводить с чужого счета.")
            return
        bank.transfer(from_account_id, to_account_id, amount)

    elif cmd == 'help':
        print('login:    Команда для авторизации пользователя\n'
              'regist:   Команда для регистрации пользователя\n'
              'add_ac:   Команда для добавления счёта\n'
              'list_aс:  Команда для просмотра всех доступных счетов\n'
              'deposit:  Команда для пополнения баланса счёта\n'
              'withdraw: Команда для снятия денег со счета\n'
              'transfer: Команда для перевода денег')


