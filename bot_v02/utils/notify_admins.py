import logging

from aiogram import Dispatcher
from data.config import admins


async def on_start_bot(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, 'Бот запущен')

        except Exception as err:
            logging.exception(err)