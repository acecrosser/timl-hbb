async def on_startup(dp):

    from utils.notify_admins import on_start_bot
    await on_start_bot(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)