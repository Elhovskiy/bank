import logging
import psycopg2
from models.account import Account
from models.customer import Customer
class Bank:
    def __init__(self, filename_account, filename_customers):
        self.filename_account = filename_account
        self.filename_customers = filename_customers
        self.customers = []
        self.accounts = {}

    def load_account(self):

        """with open(self.filename_account, 'r', encoding="utf-8") as file:
            for line in file:
                print(f"📂 Загружаем строку: {line.strip()}")
                account_number, owner, balance = line.strip().split(", ")
                balance = float(balance)
                self.accounts[account_number] = Account(account_number, owner, balance, self)
                print(f"✅ Загружен: {account_number} | {owner} | Баланс: {balance}")

        for acc_number, account in self.accounts.items():
            for customer in self.customers:
                if account.owner == customer.name:
                    customer.add_account(account, acc_number)
                    print(f"Привязан счет {acc_number} к клиенту {customer.name}")"""

    def load_customers(self):
        with open(self.filename_customers, 'r', encoding="utf-8") as file:
            for line in file:
                print(f"📂 Загружаем строку: {line.strip()}")
                customer_id, name, password = line.strip().split(", ")
                customer = Customer(name, customer_id, password)
                self.customers.append(customer)


    def save_accounts(self):
        with open(self.filename_account, 'w', encoding="utf-8") as file:
            for acc_number, account in self.accounts.items():
                file.write(f"{acc_number}, {account.owner}, {account.balance}\n")

    def save_customer(self):
        with open(self.filename_customers, 'w', encoding="utf-8") as file:
            for customer_id, customer in self.accounts.items():
                file.write(f"{customer_id}, {customer.name}, {customer.password}\n")


    def add_customer(self, customer):
        self.customers.append(customer)
        self.accounts.update(customer.accounts)
        print(dict(self.accounts))
        print(f'Добавлен новый клиент{customer.name}')

    def transfer(self, from_account_id, to_account_id, amount):

        from_account = self.accounts.get(from_account_id)
        to_account = self.accounts.get(to_account_id)

        if from_account is None:
            raise ValueError(f"❌ Ошибка: не найден счет {from_account_id}")
        if to_account is None:
            raise ValueError(f"❌ Ошибка: не найден счет {to_account_id}")

        from_account.withdraw(amount)
        to_account.deposit(amount)
        self.save_accounts()

        logging.info(f"Выполнен перевод ${amount} c ${from_account.account_number} на ${to_account.account_number}")
        print(f'Перевод средств с {from_account.account_number} на {to_account.account_number}: ${amount}')