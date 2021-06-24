from aiogram.dispatcher.filters.state import State, StatesGroup

class Profile(StatesGroup):
    age = State()
    gender = State()
    agreement = State()
    change_lan = State()