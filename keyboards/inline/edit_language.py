from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import flag

change_lan = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text=f"English {flag.flag('US')}", callback_data="lan_en"),
                InlineKeyboardButton(text=f"Русский {flag.flag('RU')}", callback_data="lan_ru"),
            ],
            # [
            #     InlineKeyboardButton(text=f"Türkçe {flag.flag('TR')}", callback_data="lan_tr"),
            #     InlineKeyboardButton(text=f"Deutsch {flag.flag('DE')}", callback_data="lan_de"),
            # ],
            # [
            #     InlineKeyboardButton(text=f"Кыргызча {flag.flag('KG')}", callback_data="lan_ky"),
            #     InlineKeyboardButton(text=f"Қазақша {flag.flag('KZ')}", callback_data="lan_kk"),
            # ],
        ]
    )