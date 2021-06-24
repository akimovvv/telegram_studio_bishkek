from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import emoji
from keyboards.inline import change_lan

from loader import dp, _
from utils.db_api import db_commands as db
from states import Profile



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await db.add_user(id=message.from_user.id, username=message.from_user.username)
    user = await db.select_user(id=message.from_user.id)
    if user.agreement == None:
        text = _("Привет, {user}!").format(user=message.from_user.full_name)
        await message.answer(text=text, reply_markup=change_lan)
        await message.edit_reply_markup()
    else:
        text = _("Привет, {user}!").format(user=message.from_user.full_name)
        await message.answer(text=text)


@dp.message_handler(commands=["language"])
async def set_language(message: types.Message):
    await db.add_user(id=message.from_user.id, username=message.from_user.username)
    user = await db.select_user(id=message.from_user.id)
    if user.agreement != None:
        await Profile.change_lan.set()
        text = _("Выберите язык!")
        await message.answer(text=text, reply_markup=change_lan)
        await message.edit_reply_markup()
    else:
        await message.answer(text='/start')


@dp.callback_query_handler(state=Profile.change_lan, text_contains="lan",)
async def set_language(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    lan = call.data[-2:]
    await db.update_user_language(id=call.from_user.id, language=lan)
    user = await db.select_user(id=call.from_user.id)
    answer = ["Вы поменяли язык!",
              "Sie haben die Sprache geändert!",
              "You've changed your language!",
              "Сіз тілді өзгерттіңіз!",
              "Сиз тилиңизди өзгөрттүңүз!",
              "Dilini değiştirdiniz!",
              ]
    if user.language == 'ru':
        await call.message.answer(text=answer[0], reply_markup=ReplyKeyboardRemove())
        await state.finish()
    elif user.language == 'en':
        await call.message.answer(text=answer[2], reply_markup=ReplyKeyboardRemove())
        await state.finish()
    # elif user.language == 'de':
    #     await call.message.answer(text=answer[1], reply_markup=ReplyKeyboardRemove())
    #     await state.finish()
    # elif user.language == 'kk':
    #     await call.message.answer(text=answer[3])
    #     await state.finish()
    # elif user.language == 'ky':
    #     await call.message.answer(text=answer[4])
    #     await state.finish()
    # elif user.language == 'tr':
    #     await call.message.answer(text=answer[5])
    #     await state.finish()




@dp.callback_query_handler(text_contains="lan")
async def change_language(call: CallbackQuery):
    await call.message.delete()
    lan = call.data[-2:]
    await db.update_user_language(id=call.from_user.id, language=lan)
    user = await db.select_user(id=call.from_user.id)
    answer = ["Вы поменяли язык!\n\nЗаполните анкету для улучшения качества услуг\n\nВведите ваш возраст...",
              "Sie haben die Sprache geändert!\n\nFüllen Sie den Fragebogen aus, um die Qualität der Dienstleistungen zu verbessern\n\nGeben Sie Ihr Alter ein...",
              "You've changed your language!\n\nFill out the questionnaire to improve the quality of services\n\nEnter your age...",
              "Сіз тілді өзгерттіңіз!\n\nҚызмет сапасын жақсарту үшін сауалнаманы толтырыңыз\n\nЖасыңызды енгізіңіз...",
              "Сиз тилиңизди өзгөрттүңүз!\n\nКызматтардын сапатын жогорулатуу үчүн форманы толтуруңуз\n\nСураныч,жашыңызды жазыныз...",
              "Dilini değiştirdiniz!\n\nHizmet kalitesini artırmak için anketi doldurun\n\nYaşınızı girin...",
              ]
    if user.language == 'ru':
        await call.message.answer(text=answer[0])
        await Profile.first()
    elif user.language == 'en':
        await call.message.answer(text=answer[2])
        await Profile.first()
    # elif user.language == 'de':
    #     await call.message.answer(text=answer[1])
    #     await Profile.first()
    # elif user.language == 'kk':
    #     await call.message.answer(text=answer[3])
    #     await Profile.first()
    # elif user.language == 'ky':
    #     await call.message.answer(text=answer[4])
    #     await Profile.first()
    # elif user.language == 'tr':
    #     await call.message.answer(text=answer[5])
    #     await Profile.first()



@dp.message_handler(state=Profile.age)
async def set_age(message: types.Message, state=FSMContext):
    answer = message.text
    try:
        if answer.isdigit():
            if int(answer) > 0 and int(answer) < 150:
                answer = int(answer)
                await state.update_data(age=answer)
                gender = InlineKeyboardMarkup(
                    inline_keyboard=
                    [
                        [
                            InlineKeyboardButton(text=_("Женский ") + emoji.emojize(":woman:"), callback_data="woman"),
                            InlineKeyboardButton(text=_("Мужской ") + emoji.emojize(":man:"), callback_data="man"),
                        ]
                    ]
                )
                await message.answer(text=_("Введите ваш пол") + emoji.emojize(":man:") + "|" + emoji.emojize(":woman:"), reply_markup=gender)
                await Profile.next()
        else:
            await message.answer(text=_("Некорректно ввели Ваш возраст, пожалуйста введите снова..."))
            await Profile.age()
    except Exception as ex:
        print(ex)



@dp.callback_query_handler(text_contains="man", state=Profile.gender)
async def set_woman(call: CallbackQuery, state: FSMContext):
    if call.data == "man":
        await call.answer(cache_time=60)
        await call.message.edit_reply_markup()
        answer = 0
        confirm = InlineKeyboardMarkup(
            inline_keyboard=
            [
                [
                    InlineKeyboardButton(text=_("Да ") + emoji.emojize(":check_mark:"), callback_data="yes"),
                ]
            ]
        )
        await state.update_data(gender=answer)
        await call.message.answer(text=_("Вы даёте согласие для обработки ваших данных?"), reply_markup=confirm)
        await Profile.next()
    elif call.data == "woman":
        await call.answer(cache_time=60)
        await call.message.edit_reply_markup()
        answer = 1
        confirm = InlineKeyboardMarkup(
            inline_keyboard=
            [
                [
                    InlineKeyboardButton(text=_("Да ") + emoji.emojize(":check_mark:"), callback_data="yes"),
                ]
            ]
        )
        await state.update_data(gender=answer)
        await call.message.answer(text=_("Вы даёте согласие для обработки ваших данных?"), reply_markup=confirm)
        await Profile.next()




@dp.callback_query_handler(lambda c: c.data == "yes", state=Profile.agreement)
async def set_agreement(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup()
    data = await state.get_data()
    u_id = call.from_user.id
    answer = 1
    age = data.get("age")
    gender = data.get("gender")
    await db.update_user(id=u_id, age=age, gender=gender, agreement=answer)
    await call.message.answer(text=_("Спасибо за заполненную анкету!\nВся введённая вами информация строго конфиденциальна и используется для улучшения наших продуктов и сервиса.\nГлавное меню /menu"))
    await state.finish()



