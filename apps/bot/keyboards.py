from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

markup_request_phone = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
    .add(KeyboardButton('Зарегистрироваться', request_contact=True))

markup_start_test = InlineKeyboardMarkup() \
    .add(InlineKeyboardButton('Начать тест', callback_data='start_test'))
