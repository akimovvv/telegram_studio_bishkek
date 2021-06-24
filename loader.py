from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from middlewares.language import setup_middleware
from utils.db_api.db_gino import db

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

i18n = setup_middleware(dp)
_ = i18n.gettext

__all__ = ["bot", "storage", "dp", "db"]