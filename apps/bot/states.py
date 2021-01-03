from aiogram.dispatcher.filters.state import StatesGroup, State


class ContactForm(StatesGroup):
    phone = State()
