import logging
class Account:
    def __init__(self,account_number,owner , balance, bank):# account number - номер счета
        self.account_number = account_number
        self.balance = balance
        self.owner = owner  # owner - владелец счета
        self.transaction = []
        self.bank = bank

    def deposit(self,amount):
        if amount <=  0:
            logging.error(f"Попытка ввести некоректную сумму на счёт ${self.account_number}: ${amount}")
            raise ValueError('Сумма депозита отрицательная')

        self.balance += amount
        self.update_balance()
        self.transaction.append(f'deposit: ${amount}')
        self.bank.save_accounts()
        logging.info(f'Депозит средств на счёт ${self.account_number}: ${amount}')

    def withdraw(self,amount):
        if amount > self.balance:
            logging.error(f"Попытка снять больше средств, чем есть на счёте ${self.account_number}: ${amount}")
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        self.update_balance()
        self.transaction.append(f'withdraw: ${amount}')
        logging.info(f'Снятие средств с счёта ${self.account_number}: ${amount}')
        self.bank.save_accounts()

    def update_balance(self):
        with self.bank.conn.cursor() as curs:
            curs.execute('UPDATE account SET balance = %s WHERE id_a = %s', (self.balance, self.account_number))
            self.bank.conn.commit()

    def transaction_history(self):
        return self.transaction
