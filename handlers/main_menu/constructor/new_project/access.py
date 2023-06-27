from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text
from handlers.main_menu.constructor.new_project import access

from handlers.main_menu.constructor.new_project.choise_work_directory import who
async def new_project(message: types.Message) -> None:
    await message.reply(text="Новый проект")


def register_handlers_new_project(dp: dispatcher):
    
    dp.register_message_handler(new_project, Text(equals='Новый проект'))
    who.register_handlers_who(dp)

    