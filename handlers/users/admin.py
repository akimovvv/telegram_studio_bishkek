from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data.config import ADMINS
from loader import dp, _, bot
from states import Mailing
from utils.db_api import db_commands as db


# Фича для рассылки по юзерам (учитывая их язык)
@dp.message_handler(user_id=ADMINS, commands=["tell"])
async def mailing(message: types.Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text=_("Да"), callback_data="yes")],
            [InlineKeyboardButton(text=_("нет"), callback_data="no")],
        ]
    )
    await message.answer(_('Вставить фото?'), reply_markup=markup)
    await Mailing.Photo.set()


@dp.callback_query_handler(user_id=ADMINS, state=Mailing.Photo)
async def mailing(call: CallbackQuery):
    await call.answer(cache_time=30)
    if call.data == 'yes':
        await call.message.answer(_('Отправьте фото в виде изображения, а не документа!'))
        await Mailing.Photo_send.set()
    else:
        await call.message.answer(_("Пришлите текст рассылки"))
        await Mailing.Text.set()
    await call.message.delete()



@dp.message_handler(user_id=ADMINS, state=Mailing.Photo_send, content_types=types.ContentTypes.PHOTO)
async def mailing(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(photo=photo)
    await message.answer(_("Пришлите текст рассылки"))
    await Mailing.Photo_text.set()



@dp.message_handler(user_id=ADMINS, state=Mailing.Photo_text)
async def mailing(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    await state.update_data(text=text)
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text="Русский", callback_data="ru")],
            [InlineKeyboardButton(text="English", callback_data="en")],
            # [InlineKeyboardButton(text="Turkce", callback_data="tr")],
        ]
    )
    await message.answer_photo(photo=data.get('photo'), caption=_("Пользователям на каком языке разослать это сообщение?\n\n"
                           "Текст:\n"
                           "{text}").format(text=text),
                         reply_markup=markup)
    await Mailing.Photo_Language.set()



@dp.message_handler(user_id=ADMINS, state=Mailing.Text)
async def mailing(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text="Русский", callback_data="ru")],
            [InlineKeyboardButton(text="English", callback_data="en")],
            # [InlineKeyboardButton(text="Turkce", callback_data="tr")],
        ]
    )
    await message.answer(_("Пользователям на каком языке разослать это сообщение?\n\n"
                           "Текст:\n"
                           "{text}").format(text=text),
                         reply_markup=markup)
    await Mailing.Language.set()

@dp.callback_query_handler(user_id=ADMINS, state=Mailing.Photo_Language)
async def mailing_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    photo = data.get('photo')
    await state.reset_state()
    await call.message.edit_reply_markup()

    users = await db.select_user_id(lan=call.data)
    for user in users:
        try:
            await bot.send_photo(chat_id=user.id, photo=photo,
                                   caption=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer(_("Рассылка выполнена."))



@dp.callback_query_handler(user_id=ADMINS, state=Mailing.Language)
async def mailing_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    await state.reset_state()
    await call.message.edit_reply_markup()

    users = await db.select_user_id(lan=call.data)
    for user in users:
        try:
            await bot.send_message(chat_id=user.id,
                                   text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer(_("Рассылка выполнена."))

