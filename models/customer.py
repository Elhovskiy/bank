from models.account import Account
class Customer:
    def __init__(self, name, customer_id, password):
        self.name = name
        self.customer_id = customer_id
        self.password = password
        self.accounts = {} # account - счет
    def add_account(self, account, number):
        self.accounts[account.account_number] = account
        print(f"Клиент {self.name}: добавлен счет {account.account_number}")