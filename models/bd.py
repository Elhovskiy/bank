import psycopg2

conn = psycopg2.connect(dbname='bank', user='postgres', password='567765', host='localhost')
def load_account():
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM customer')
        curs.fetchall()

print(load_account())