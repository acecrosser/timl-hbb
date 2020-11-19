import logging
import psycopg2 as sql
from typing import Dict
from datetime import datetime

sql.OperationalError()

connect = sql.connect(dbname='db_finbot',
                      user='bot_admin',
                      password='PmeT3mn7tPynhVqY254M',
                      host='localhost', port='5432')
cursor = connect.cursor()
connect.autocommit = True


def make_default_db():
    cursor.execute('CREATE TABLE profit '
                   '(id_user integer, amount real, grouping text, title text, time text)')
    cursor.execute('CREATE TABLE expense '
                   '(id_user integer, amount real, grouping text, title text, time text)')
    connect.commit()
    print('БД успешно создана')


def insert_data(table: str, column_items: Dict):
    columns = ', '.join(column_items.keys())
    values = tuple(column_items.values())
    number = ', '.join(['%s'] * len(column_items.keys()))
    cursor.execute(
        f'INSERT INTO {table} '
        f'({columns})'
        f'VALUES ({number})', values)
    logging.info('Данные успешно внесены...')


def today(table: str, id_user: str, period: str):
    cursor.execute(
        f"SELECT sum(amount) FROM {table} WHERE id_user='{id_user}' AND time LIKE'{period}%'"
    )
    summa_today = cursor.fetchone()
    return summa_today


if __name__ == '__main__':
    make_default_db()
