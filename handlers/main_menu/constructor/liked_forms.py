from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text

from lib import handler
 


async def liked_forms(message: types.Message) -> None:
    await message.reply(text="любимые формы")


def register_handlers_liked_forms(dp: dispatcher):
    
    dp.register_message_handler(liked_forms, Text(equals='Любимые формы'))
    