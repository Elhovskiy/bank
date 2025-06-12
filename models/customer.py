from models.account import Account
from typing import Literal

class Customer:
    def __init__(self, customer_id, name, password):
        self.customer_id: str = customer_id
        self.name: str = name
        self.password: str = password
        self.accounts: dict[str, str] = {}  # account - счет

    def add_account_customer(self, account):
        self.accounts[account.account_number] = account
