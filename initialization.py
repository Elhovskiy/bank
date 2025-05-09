from models.bank import Bank
from models.customer import Customer
from models.account import Account
from interface import command_interface
import logging

def create_bank_system():
    bank = Bank("account.txt", "customer.txt")

    bank.load_customers()
    bank.load_account()

    return bank
def run_bank():
        logging.basicConfig(level=logging.INFO,
                            filename='logging.log',
                            filemode='w',
                            format='%(asctime)s - %(levelname)s - %(message)s')
        while True:
            command = input("Введите комманду: (или exit для выхода) ").strip()
            if command == "exit":
                break
            bank = create_bank_system()
            command_interface(command,bank)