class Authentication:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def authentication(self, name: str, password: str):
        for customer in self.bank.customers:
            if customer.name == name and customer.password == password:
                self.current_user = customer
                print("Аутентификая успешна")
                return
        raise Exception('Неверные учетные данные')
    def user_verification(self, account_number):
        if not self.current_user:
            print("Вы не вошли в систему")
            return False
        return account_number == self.current_user.accounts