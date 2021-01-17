from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from apps.bot import test_categories

markup_request_phone = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
    .add(KeyboardButton('Зарегистрироваться', request_contact=True))

markup_menu = ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(KeyboardButton('Профиль'), KeyboardButton('Тесты'), KeyboardButton('Халява'))

markup_test_categories = ReplyKeyboardMarkup(resize_keyboard=True).add(*test_categories.categories)

