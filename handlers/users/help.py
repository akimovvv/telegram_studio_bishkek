from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import ADMINS
from loader import dp, _


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = '1'
    for admin in ADMINS:
        if int(message.from_user.id) == int(admin):
            print(admin)
            text = _("Список команд:\n"
                     "/start - Начать диалог\n"
                     "/menu - Главное меню\n"
                     "/tell - Рассылка\n"
                     "/language - Смена языка\n"
                     "/help - Получить справку")
            text = text
        else:
            text = _("Список команд:\n"
                     "/start - Начать диалог\n"
                     "/menu - Главное меню\n"
                     "/language - Смена языка\n"
                     "/help - Получить справку")
            text = text
    await message.answer(text=text)



# @dp.message_handler(CommandHelp())
# async def bot_help(message: types.Message):
#     text = ("Список команд: ",
#             "/start - Начать диалог",
#             "/help - Получить справку")
#
#     await message.answer("\n".join(text))