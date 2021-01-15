import logging
from .connect import cursor


def list_settings(id_user: str, grouping: str) -> list:
    cursor.execute(
        f"SELECT title "
        f"FROM settings "
        f"WHERE id_user='{id_user}' AND grouping='{grouping}'"
    )
    settings = cursor.fetchall()
    return settings


def add_setting(id_user: str, title: str, grouping: str):
    cursor.execute(
        f"INSERT INTO settings (id_user, title, grouping) "
        f"VALUES ('{id_user}', '{title}', '{grouping}')"
    )
    logging.info('Группа добавлена')


def del_setting(id_user: str, title: str):
    cursor.execute(
        f"DELETE FROM settings "
        f"WHERE title='{title}' "
        f"AND id_user='{id_user}'"
    )
    logging.info('Группа удалена')

