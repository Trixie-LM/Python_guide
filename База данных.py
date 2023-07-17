import psycopg2


# Настройки базы данных
database = "lottery"
user_database = "lottery"
password_database = "lottery"
host = "postgres1.dev.int.nl-dev.ru"
port = "5432"

con = psycopg2.connect(
    database=database,
    user=user_database,
    password=password_database,
    host=host,
    port=port
)
print("Database opened successfully")

cur = con.cursor()

def mapping(select_number):
    cur.execute(select_number)
    print(cur.fetchone())


# mapping(config.ticket_set_number)


cur.close()
