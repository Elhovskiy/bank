from models.account import Account
class Customer:
    def __init__(self, customer_id, name, password):
        self.customer_id = customer_id
        self.name = name
        self.password = password
        self.accounts = {} # account - счет
    def add_account_customer(self, account):
        self.accounts[account.account_number] = account