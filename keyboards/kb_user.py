from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton







def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Любимые формы'))
    kb.add(KeyboardButton('Мои проекты'))
    kb.add(KeyboardButton('Новый проект'))
    kb.add(KeyboardButton('Прикрутить домен'))
    return kb

def choose_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Конструктор PRACTICE'), KeyboardButton('Мероприятия'), KeyboardButton('Галерея'), KeyboardButton('Что такое PRACTICE?'), KeyboardButton('Обратная связь'))
    return kb

def event_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Интенсив ПРАКТИС'), KeyboardButton('КОД ИБ + ПРАКТИС'))
    return kb

def games_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('CS:GO')).add(KeyboardButton('DOTA 2'))
    return kb

def cancle_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Вернуться обратно'))
    return kb


def want_to_team() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('О PRACTICE')).add(KeyboardButton('Хочу в команду'))
    return kb

def link() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True)
    kb.add(InlineKeyboardButton(text='Написать', url='https://t.me/skyfox1994', callback_data='link'))
    return kb