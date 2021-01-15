import psycopg2 as sql
from data import config

sql.OperationalError()

connect = sql.connect(dbname=config.DB_NAME,
                      user=config.USER,
                      password=config.PASSWD,
                      host='localhost', port='5432')
cursor = connect.cursor()
connect.autocommit = True


def make_default_db():
    cursor.execute('CREATE TABLE profit '
                   '(id_user integer, amount real, grouping text, title text, time text)')
    cursor.execute('CREATE TABLE expense '
                   '(id_user integer, amount real, grouping text, title text, time text)')
    cursor.execute('CREATE TABLE settings '
                   '(id_user integer, title text, grouping text)')
    connect.commit()
    print('БД успешно создана')


if __name__ == '__main__':
    make_default_db()
