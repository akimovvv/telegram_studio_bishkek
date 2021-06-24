from aiogram import executor

from loader import dp, db
import asyncio
import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.notify_admins import on_startup_notify

async def on_startup(dispatcher):
    # # Уведомляет про запуск
    # await asyncio.sleep(10)
    await db_gino.on_starup(dispatcher)
    await db.gino.create_all()
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
