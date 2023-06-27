from aiogram import types, dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text



async def my_project(message: types.Message) -> None:
    await message.reply(text="Мои проекты")


def register_handlers_my_progect(dp: dispatcher):
    
    dp.register_message_handler(my_project, Text(equals='Мои проекты'))
    