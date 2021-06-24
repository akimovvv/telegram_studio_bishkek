from aiogram.dispatcher.filters.state import State, StatesGroup

class Main(StatesGroup):
    about_us = State()
    services = State()
