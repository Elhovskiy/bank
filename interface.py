import argparse
from models.auth import Authentication

def command_interface(command,bank):
    auth = Authentication(bank)
    args = command.split()
    if not args:
        return
    cmd = args[0]

    if cmd == 'login':
        auth.authentication(args[1], args[2])
    elif cmd == 'deposit':
        account = bank.accounts.get(args[1])
        account.deposit(int(args[2]))
    elif cmd == 'withdraw':
        account = bank.accounts.get(args[1])
        if not auth.user_verification(account):
            print("�� Недоступен для операции с этим счетом.")
            return
        account.withdraw(int(args[2]))
    elif cmd == 'transfer':
        from_account_id = args[1]
        to_account_id = args[2]
        amount = int(args[3])
        if not auth.user_verification(from_account_id):
            print("�� Недоступен для операции с этим счетом.")
            return
        print(f"🔍 Передача средств: {args[2]} → {args.to_ac[3]}, сумма {args[4]}")
        bank.transfer(from_account_id, to_account_id, amount)

    """auth = Authentication(bank)
    parser = argparse.ArgumentParser(description='Банк')
    subparsers = parser.add_subparsers(dest="command")

    login = subparsers.add_parser("login")
    login.add_argument("--name", help="Имя клиента")
    login.add_argument("--password", help="Пароль")

    deposit = subparsers.add_parser("deposit")
    deposit.add_argument("--account", type=str, help="Номер счета")
    deposit.add_argument("--amount", type=int, help="Сумма пополнения")

    withdraw = subparsers.add_parser("withdraw")
    withdraw.add_argument("--account", type=str, help="Номер счета")
    withdraw.add_argument("--amount", type=int, help="Сумма снятия")

    transfer = subparsers.add_parser("transfer")
    transfer.add_argument("--from_ac", required=True, help="Номер исходного счета")
    transfer.add_argument("--to_ac", required=True, help="Номер получателя")
    transfer.add_argument("--amount", type=int
                          , help="Сумма перевода")

    history = subparsers.add_parser("history")
    history.add_argument("--account", type=str, help="Номер счета")

    args = parser.parse_args()

    if args.command == "login":
        auth.authentication(args.name, args.password)
    elif args.command == "deposit":
        account = bank.accounts.get(args.account)
        print("Содержимое bank.accounts:", bank.accounts)
        print("Тип account:", type(account))
        account.deposit(args.amount)
    elif args.command == "withdraw":
        if not auth.user_verification(args.account):
            print("�� Недоступен для операции с этим счетом.")
            return
        account = bank.accounts.get(args.account)
        account.withdraw(args.amount)
    elif args.command == "transfer":
        if not auth.user_verification(args.from_ac):
            print("�� Недоступен для операции с этим счетом.")
            return
        print("📋 Доступные счета в банке:", bank.accounts.keys())
        print(f"🔍 Передача средств: {args.from_ac} → {args.to_ac}, сумма {args.amount}")
        print(f"🔍 Проверяем счета: {list(bank.accounts.keys())}")
        print(f"🔍 Найденный from_account: {bank.accounts.get(args.from_ac)}")
        print(f"🔍 Найденный to_account: {bank.accounts.get(args.to_ac)}")
        bank.transfer(args.from_ac,args.to_ac, args.amount)
    else:
        parser.print_help()"""

