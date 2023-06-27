from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text



async def take_domen(message: types.Message) -> None:
    await message.reply(text="Прикрутить домен")


def register_handlers_take_domen(dp: dispatcher):
    
    dp.register_message_handler(take_domen, Text(equals='Прикрутить домен'))
    