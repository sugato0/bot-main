from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text

from handlers.main_menu.constructor.new_project import new_project_register
from handlers.main_menu.constructor import liked_forms,my_projects,take_domen,constructor_register

from lib import handler
 


async def new_project(message: types.Message) -> None:
    keyboard = types.InlineKeyboardMarkup()
    keys = ["Выберите болванку","Доступ"]
    for i in keys:
        keyboard.add(types.InlineKeyboardButton(text = i,callback_data=i))
    await message.reply(text="Новый проект",reply_markup=keyboard)


def register_handlers_new_project(dp: dispatcher):
    
    dp.register_message_handler(new_project, Text(equals='Новый проект'))
    new_project_register.register_handlers_new_project(dp)
    liked_forms.register_handlers_liked_forms(dp)
    my_projects.register_handlers_my_progect(dp)
    take_domen.register_handlers_take_domen(dp)
    