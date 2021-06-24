from aiogram.dispatcher.filters.state import State, StatesGroup

class Make_order(StatesGroup):
    get_contact = State()
    get_description = State()