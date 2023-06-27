from aiogram import types, dispatcher

from handlers.main_menu.constructor.new_project.choise_work_directory import who
from aiogram.dispatcher.filters import Text

from lib import handler
 


async def bolvanka(call: types.CallbackQuery) -> None:
    keyboard = types.InlineKeyboardMarkup()
    keys = ["Типирование","Практис","Понарт","Чистый лист"]
    for i in keys:
        keyboard.add(types.InlineKeyboardButton(text = i,callback_data=i))
    await call.message.reply(text="болванка",reply_markup=keyboard)


def register_handlers_new_project(dp: dispatcher):
    
    dp.register_callback_query_handler(bolvanka, Text(equals='Выберите болванку'))
    who.register_handlers(dp)