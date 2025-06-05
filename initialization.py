from models.bank import Bank
from models.customer import Customer
from models.account import Account
from interface import command_interface
from models.auth import Authentication
import logging

def create_bank_system():
    bank = Bank("account.txt")

    return bank
def run_bank():
        logging.basicConfig(level=logging.INFO,
                            filename='logging.log',
                            filemode='w',
                            format='%(asctime)s - %(levelname)s - %(message)s')

        bank = create_bank_system()
        auth = Authentication(bank)
        print('Авторизируйтесь или зарегиструйтесь для взаимодейсвия\n'
              '(введите команду help для демонстрации возможных команд)')
        while True:
            command = input("Введите комманду: (или exit для выхода) ").strip()
            if command == "exit":
                break
            command_interface(command,bank, auth)