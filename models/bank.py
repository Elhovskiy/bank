import logging
import psycopg2
import os
from dotenv import load_dotenv
from models.auth import Authentication
from models.customer import Customer
from models.account import Account

load_dotenv()

class Bank:
    def __init__(self):
        self.customer = []
        self.accounts = {}
        try:
            self.conn = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), host=os.getenv('HOST'))
        except:
            print("❌ Введены неправельные данные для подключения БД")

    def load_account(self):
        for customer in self.customer:
            with self.conn.cursor() as curs:
                curs.execute('SELECT * FROM account WHERE id_c=%s', (customer.customer_id,))
                self.conn.commit()
                row = curs.fetchone()
                if row:
                    self.accounts[str(row[0])] = Account(row[0], customer.name, row[1], self)
                    for acc_number, account in self.accounts.items():
                        customer.add_account_customer(account)
                else:
                    logging.error(f"❌ Ошибка при загрузки счёта ")

    def add_account_bd(self):
        with self.conn.cursor() as curs:
            try:
                curs.execute('INSERT INTO account (balance, id_c) VALUES (%s, %s)', (0, self.customer[0].customer_id))
                self.load_account()
                print('✅ Новый счет успешно добавлен' )
            except:
                logging.error("❌ Ошибка при добавлении нового счета счёта ")
                raise Exception("❌ Ошибка при добавлении нового счета счёта ")

    def list_of_account(self):
        if self.accounts:
            for acc_number, account in self.accounts.items():
                print(f'Cчёт: {acc_number} Баланс: {account.balance}')
        else:
            print('У вас пока нет ни одного счета')

    def transfer(self, from_account_id, to_account_id, amount):

        from_account = self.accounts.get(from_account_id)
        to_account = self.accounts.get(to_account_id)

        if from_account is None:
            raise ValueError(f"❌ Ошибка: не найден счет {from_account_id}")
        if to_account is None:
            raise ValueError(f"❌ Ошибка: не найден счет {to_account_id}")

        from_account.withdraw(amount)
        to_account.deposit(amount)
        logging.info(f"Выполнен перевод ${amount} c ${from_account.account_number} на ${to_account.account_number}")
        print(f'Перевод средств с {from_account.account_number} на {to_account.account_number}: ${amount}')