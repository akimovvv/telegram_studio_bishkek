from aiogram.dispatcher import FSMContext

from loader import dp, _
from aiogram import types
import emoji
from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery
from states import Main, Make_order




@dp.message_handler(commands=['menu'])
async def main_menu(message: types.Message):
    main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
        [
            KeyboardButton(text=_("Услуги  ") + emoji.emojize(':construction_worker:'))
        ],
        [
            KeyboardButton(text=_("О нас  ") + emoji.emojize(':thought_balloon:'))
        ]
    ])
    await message.answer(text=_("Главное меню"), reply_markup=main_menu_keyboard)



@dp.message_handler(text=("Услуги  " + emoji.emojize(':construction_worker:'), "Services  "  + emoji.emojize(':construction_worker:')))
async def service(message: types.Message):
    service = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Базовый") + "  " + emoji.emojize(':robot:'), callback_data='base_bot'),
            InlineKeyboardButton(text=_("Средний") + "  " + emoji.emojize(':robot:'), callback_data='medium_bot')
        ],
        [
            InlineKeyboardButton(text=_("Индивидуальный") + "  " + emoji.emojize(':robot:'), callback_data='individual_bot')
        ],
        [
            InlineKeyboardButton(text=_("Другие виды услуг") + "  " + emoji.emojize(':robot:'),
                                 callback_data='another_service')
        ],
        [
            InlineKeyboardButton(text=_("Главное меню"), callback_data="menu")
        ]
    ])
    caption = _("Telegram Studio Bishkek предоставляет комплексную услугу разработки функциональных "
                "ботов для Telegram, также у нас можно купить бота телеграмм.\n\nМессенджер Telegram "
                "лавинообразно набирает популярность по всему миру. Пользователи отдают ему "
                "предпочтение из-за безопасности, анонимности, удобства, а также возможности "
                "использования функциональных чат ботов.")
    await message.reply_photo(photo='AgACAgIAAxkBAAIDkWDNgWGg-3X0yjhv_ey-etnvVyl9AAItszEbUKJxSmtYJetLZX1SUNQppC4AAwEAAwIAA3MAA-tqAgABHwQ',caption=caption, reply_markup=service)



@dp.callback_query_handler(lambda c: c.data == "base_bot")
async def frequent_questions(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Telegram Бот с базовым функционалом</b>\n\n"
             "<b>Функции:</b>\nМногоязычность: 2 языка на выбор.\nРассылка: Пользователям Бота.\n"
             "Данные о пользователей: кол-во + одна функция на выбор\n\n"
             "<b>Пример базовых Ботов</b>\nБот визитка\nБот для сбора заявок\nБот для анкетирования и тд.\n\n"
             "<b>Узнать подробнее:</b>\nМожете оставить заявку или позвонить|написать"
             )
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Контакты"), callback_data="contacts"),
            InlineKeyboardButton(text=_("Оставить заявку"), callback_data="make_order1")
        ],
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == "another_service")
async def frequent_questions(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Так же мы можем разработать вам других ботов</b>\n\n"
             "<b>Например:</b>\nБот для рассылки (WhatsApp, Telegram, Instagram, Facebook и тд.)\nБот для раскрутки TikTok,Instagram(автоподписка, лайки, отписка и тд.)\n"
             "Парсеры данных(с сайтов и тд.)\n\n"
             "<b>Узнать подробнее:</b>\nМожете оставить заявку или позвонить|написать"
             )
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Контакты"), callback_data="contacts"),
            InlineKeyboardButton(text=_("Оставить заявку"), callback_data="make_order4")
        ],
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == "medium_bot")
async def frequent_questions(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Telegram Бот со средним функционалом</b>\n\n"
             "<b>Функции:</b>\nМногоязычность: 3 языка на выбор.\n"
             "Сбор данных(анкетирование) и регистрация пользователей.\nРассылка: Пользователям Бота.\n"
             "Данные о пользователей: кол-во + две функции на выбор\n\n"
             "<b>Пример средних Ботов</b>\nБот магазин с хорошим функционалом\nБот технической поддержки\nБот приёма заказов с обширным функционалом и тд.\n\n"
             "<b>Узнать подробнее:</b>\nМожете оставить заявку или позвонить|написать"
             )
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Контакты"), callback_data="contacts"),
            InlineKeyboardButton(text=_("Оставить заявку"), callback_data="make_order2")
        ],
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)

@dp.callback_query_handler(lambda c: c.data == "individual_bot")
async def frequent_questions(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Telegram Бот с индивидуальным функционалом</b>\n\n"
             "<b>Функции:</b>\nОбговаривается индивидуально. Мы разрабатываем проект используя лучшие технологии на рынке.\n\n"
             "<b>Узнать подробнее:</b>\nМожете оставить заявку или позвонить|написать"
             )
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Контакты"), callback_data="contacts"),
            InlineKeyboardButton(text=_("Оставить заявку"), callback_data="make_order3")
        ],
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)





@dp.message_handler(text=("О нас  " + emoji.emojize(':thought_balloon:'), "About us  " + emoji.emojize(':thought_balloon:')))
async def about_us(message: types.Message):
    about_us = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Что такое телеграм бот?"), callback_data='what_bot')
        ],
        [
            InlineKeyboardButton(text=_("Почему именно мы?"), callback_data='why_we')
        ],
        [
            InlineKeyboardButton(text=_("Почему стоит заказать телеграм бота?"), callback_data='why_order')
        ],
        [
            InlineKeyboardButton(text=_("Частые вопросы..."), callback_data='frequent_questions')
        ],
        [
            InlineKeyboardButton(text=_("Наши проекты"), callback_data='our_project')
        ],
        [
            InlineKeyboardButton(text=_("Контакты"), callback_data="contacts"),
            InlineKeyboardButton(text=_("Способы оплаты"), callback_data="additional_information")
        ],
        [
            InlineKeyboardButton(text=_("Главное меню"), callback_data="menu")
        ]
    ])
    caption = _("Telegram Studio Bishkek предоставляет комплексную услугу разработки функциональных "
                "ботов для Telegram, также у нас можно купить бота телеграмм. Мессенджер Telegram "
                "лавинообразно набирает популярность по всему миру. Пользователи отдают ему "
                "предпочтение из-за безопасности, анонимности, удобства, а также возможности "
                "использования функциональных чат ботов.")
    await message.reply_photo(photo='AgACAgIAAxkBAAIDjWDNetPUAUdrHyX_mrGPBG9CYKbCAAInszEbUKJxSpyfuuw17iN3o5EHoi4AAwEAAwIAA3MAA0O6AwABHwQ', caption=caption, reply_markup=about_us)




@dp.callback_query_handler(lambda c: c.data == "what_bot")
async def what_bot(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Что такое чат бот?</b>\n\nЧат боты — это программы цель которых автоматизировать процессы "
             "и минимизировать участие людей. Они выполняют рутинные задачи практически любой сложности: "
             "поиск и выдача информации, "
             "ответы на вопросы клиентов, построение потока работы (workflow) — цепочки действий в "
             "зависимости от действия клиента или процессов внутри компании. По сути, возможности "
             "чат бота ограничены возможностями языка, на котором он создается, а это решение "
             "практически любых задач.\n\n\nФункционал Telegram (каналы, боты и чаты) способен вывести "
             "ваш бизнес на новый уровень.\n\n\nВладельцы бизнеса сегодня активно интегрируют в свои "
             "процессы чат боты telegram, ведь такой бот может не только автоматизировать процессы, "
             "исключить рутину, ожидания, но и значительно увеличить объем продаж товаров или услуг."
             )
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == "why_we")
async def why_we(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Почему мы лучшие в сфере создания чат ботов:</b>\n\nМы не используем посреднических сервисов, "
             "наши боты пишутся на python 3.9, и библиотекой aiogram который обращается напрямую к "
             "официальному API telegram. Таким образом, бот (файлы) принадлежит вам и нет рисков, что сервис посредник "
             "закроется и бот перестанет работать или изменятся условия его использования."
             " Концепт-решение бота имеет сложную логику. Мы составляем схему бота и "
             "пишем техническое задание, согласовываем все пункты с клиентом и учитываем все "
             "детали. Таким образом, получается полноценное техническое задание.")
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)





@dp.callback_query_handler(lambda c: c.data == "why_order")
async def why_order(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Почему стоит заказать телеграм бота?</b>\n\n"
             "бюджет разработки чат бота telegram в разы меньше разработки мобильного приложения;"
             "чат бот не нужно скачивать, а это экономия времени и ресурсов;"
             "чат бот работает «здесь и сейчас».")
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)





@dp.callback_query_handler(lambda c: c.data == "frequent_questions")
async def frequent_questions(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    text = _("<b>Частые вопросы и ответы по телеграм боту</b>\n\n"
             "Как происходит заказ бота? После того, как вы подробно описали необходимые функции мы формируем цену и "
             "срок разработки. Если срок и стоимость подходит, заключаем соглашение, выставляем счет на аванс "
             "в размере 50% от стоимости и приступаем к созданию технического задания и дальнейшего создания бота. "
             "По окончанию работы демонстрируем бота (также демонстрируем в процессе), выставляем "
             "счет на остаток суммы, после получения оплаты передаем файлы бота."
             )
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Если дочитал нажми сюда  ")+emoji.emojize(":check_mark:"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=text, reply_markup=delete)





@dp.callback_query_handler(lambda c: c.data == "delete", state=Main.about_us)
async def delete_inline_keyboard(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await state.finish()



@dp.callback_query_handler(lambda c: c.data == "menu")
async def delete_inline_keyboard(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer(text=_("Главное меню /menu"))




@dp.callback_query_handler(lambda c: c.data == 'contacts', state=Main.about_us)
async def send_us_num(call: CallbackQuery):
    contacts = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f'{emoji.emojize(":telephone:")} WhatsApp', url='https://api.whatsapp.com/send?phone=996500060402'),
            InlineKeyboardButton(text=f'{emoji.emojize(":telephone:")} Telegram', url='https://t.me/arturkgz')
        ],
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.answer(cache_time=30, text=_("Telegram Studio Bishkek\n\nРазработка бота\nвашей мечты!\n") + emoji.emojize(':smile:', use_aliases=True), show_alert=True)
    await call.message.answer(text=_('Нажмите как вы хотите связаться'), reply_markup=contacts)
    await call.message.delete()



@dp.callback_query_handler(text_contains="make_order", state=Main.about_us)
async def send_us_num(call: CallbackQuery, state: FSMContext):
    order_type = call.data[-1:]
    if int(order_type) == 1:
        await state.update_data(order_type='Базовый бот')
    elif int(order_type) == 2:
        await state.update_data(order_type='Средний бот')
    elif int(order_type) == 3:
        await state.update_data(order_type='Индивидуальный бот')
    elif int(order_type) == 4:
        await state.update_data(order_type='Другой вид ботов')
    get_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
            [
                KeyboardButton(text=_("Поделиться контактом"), request_contact=True)
            ]
            ])
    await call.answer(cache_time=30, text=_("Вы даёте согласие на обработку введённых вами данных?"), show_alert=True)
    await call.message.answer(text=_('Поделитесь контактом чтоб с вами могли связаться'), reply_markup=get_contact)
    await Make_order.get_contact.set()


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=Make_order.get_contact)
async def get_contact(message: types.Message, state: FSMContext):
    number = message.contact
    username = message.from_user.username
    await state.update_data(number=number)
    await state.update_data(username=username)
    await message.answer(text=_('Напишите описание бота которого вы хотите'), reply_markup=ReplyKeyboardRemove())
    await Make_order.get_description.set()



@dp.message_handler(state=Make_order.get_description)
async def get_description(message: types.Message, state: FSMContext):
    description = message.text
    data = await state.get_data()
    a = data.get('number')
    await message.bot.send_message(chat_id='-1001393623755', text=f"Вид бота: {data.get('order_type')}\nПользователь: @{data.get('username')}\nКонтакт: {a['phone_number']}\nИмя: {a['first_name']}\n\n\nОписание: {description}")
    await message.answer(text=_("Спасибо за ваш интерес!\nКак обработают вашу заявку вам напишут или позвонят") + ' ' + emoji.emojize(':smile:', use_aliases=True) + '!\n\n' + _('Главное меню /menu'))
    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'contacts')
async def send_us_num(call: CallbackQuery):
    await Main.about_us.set()
    contacts = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f'{emoji.emojize(":telephone:")} WhatsApp', url='https://api.whatsapp.com/send?phone=996500060402'),
            InlineKeyboardButton(text=f'{emoji.emojize(":telephone:")} Telegram', url='https://t.me/arturkgz')
        ],
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.answer(cache_time=30, text=_("Telegram Studio Bishkek\n\nРазработка бота\nвашей мечты!\n") + emoji.emojize(':smile:', use_aliases=True), show_alert=True)
    await call.message.answer(text=_('Нажмите как вы хотите связаться'), reply_markup=contacts)



@dp.callback_query_handler(lambda c: c.data == "additional_information")
async def additional_information(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Visa") + ' ' + emoji.emojize(':dollar:', use_aliases=True), callback_data="visa"),
            InlineKeyboardButton(text=_("DemirBank") + ' ' + emoji.emojize(':dollar:', use_aliases=True),
                                 callback_data="demir"),
            # InlineKeyboardButton(text=_("Qiwi") + ' ' + emoji.emojize(':dollar:', use_aliases=True), callback_data="qiwi"),
        ],
        [
            InlineKeyboardButton(text=_("Мой O") + ' ' + emoji.emojize(':dollar:', use_aliases=True), callback_data="moi_o"),
            InlineKeyboardButton(text=_("Элсом") + ' ' + emoji.emojize(':dollar:', use_aliases=True), callback_data="elsom"),
        ],
        # [
        #     InlineKeyboardButton(text=_("DemirBank") + ' ' + emoji.emojize(':dollar:', use_aliases=True), callback_data="demir"),
        # ],
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=_("<b>Способы оплаты</b>") + ' ' + emoji.emojize(':moneybag:', use_aliases=True), reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == 'visa', state=Main.about_us)
async def visa(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=f"{emoji.emojize(':credit_card:', use_aliases=True)}   <b>VISA</b>   {emoji.emojize(':credit_card:', use_aliases=True)}\n4172 2100 7973 0742", reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == 'demir', state=Main.about_us)
async def demir(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=f"{emoji.emojize(':credit_card:', use_aliases=True)}   <b>Demir Bank</b>   {emoji.emojize(':credit_card:', use_aliases=True)}\n1180 0001 3252 5044", reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == 'moi_o', state=Main.about_us)
async def moi_o(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=f"{emoji.emojize(':credit_card:', use_aliases=True)}   <b>Мой O</b>   {emoji.emojize(':credit_card:', use_aliases=True)}\n0 500 06 04 02", reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == 'elsom', state=Main.about_us)
async def elsom(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=f"{emoji.emojize(':credit_card:', use_aliases=True)}   <b>Элсом</b>   {emoji.emojize(':credit_card:', use_aliases=True)}\n0 990 55 01 25", reply_markup=delete)




@dp.callback_query_handler(lambda c: c.data == "our_project")
async def our_project(call: CallbackQuery):
    await Main.about_us.set()
    await call.answer(cache_time=30)
    delete = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("YouTube"), url='https://www.youtube.com/channel/UC3x_gJqjP5Yw3nr88YI6YsQ', callback_data="youtube")],
        [
            InlineKeyboardButton(text=_("Назад"), callback_data="delete")
        ]
    ])
    await call.message.answer(text=_("Наши проекты и так же примеры и варианты выполнения"), reply_markup=delete)
