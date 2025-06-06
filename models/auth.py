import psycopg2
import hashlib
from models.customer import Customer
class Authentication:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def registration(self, name: str, password: str):
        with self.bank.conn.cursor() as curs:
            curs.execute('INSERT INTO customer (name, password) VALUES(%s, %s);', (name, hashlib.sha256(password.encode()).hexdigest()))
            self.bank.conn.commit()
            print('✅ Вы успешно зарегистрировались. Войдите чтобы продолжить!')

    def authentication(self, name: str, password: str):
        with self.bank.conn.cursor() as curs:
            curs.execute('SELECT * FROM customer WHERE name=%s AND password=%s', (name, hashlib.sha256(password.encode()).hexdigest()))
            self.bank.conn.commit()
            row = curs.fetchone()
            if row:
                self.current_user = Customer(row[0], row[1], row[2])
                self.bank.customer.append(self.current_user)
                print(f"✅ Аутентификация успешна. Добро пожаловать, {name}!")
            else:
                raise Exception("❌ Аутентификация не пройдена. Проверьте имя и пароль.")

    def checking_user_authentication(self):
        if not self.current_user:
            print("❌ Вы не вошли в систему.")
            return False
        return True
