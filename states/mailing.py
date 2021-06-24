from aiogram.dispatcher.filters.state import State, StatesGroup

class Mailing(StatesGroup):
    Text = State()
    Language = State()
    Photo = State()
    Photo_send = State()
    Photo_text = State()
    Photo_Language = State()