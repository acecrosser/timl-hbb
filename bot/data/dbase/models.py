import logging
from typing import Dict
from .connect import cursor


def insert_data(table: str, column_items: Dict):
    columns = ', '.join(column_items.keys())
    values = tuple(column_items.values())
    number = ', '.join(['%s'] * len(column_items.keys()))
    cursor.execute(
        f'INSERT INTO {table} '
        f'({columns})'
        f'VALUES ({number})', values)
    logging.info('Insert in db: Success')


def today(table: str, id_user: str, period: str):
    cursor.execute(
        f"SELECT sum(amount) "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND time LIKE '{period}%'"
    )
    summa_today = cursor.fetchone()
    return summa_today


def distinct(name: str, table: str, id_user: str, period: str):
    cursor.execute(
        f"SELECT DISTINCT {name} "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND time LIKE '{period}%'"
    )
    distinct_data = cursor.fetchall()
    return distinct_data


def sum_title(table: str, id_user: str, period: str, grouping: str, name: str) -> float:
    cursor.execute(
        f"SELECT SUM(amount) "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND {name} LIKE '{grouping}%' "
        f"AND time LIKE '{period}%'"
    )
    title_sum = cursor.fetchone()
    return title_sum


def distinct_group(title: str, table: str, id_user: str, period: str, grouping: str):
    cursor.execute(
        f"SELECT {title}, amount "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND grouping='{grouping}' "
        f"AND time LIKE '{period}%'"
    )
    distinct_data = cursor.fetchall()
    return distinct_data


def disctinc_title(table: str, id_user: str, grouping: str, period: str):
    cursor.execute(
        f"SELECT DISTINCT title "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND grouping='{grouping.lower()}' "
        f"AND time LIKE '{period}%'"
    )
    return cursor.fetchall()
