from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text

from handlers.main_menu.constructor.new_project.choise_work_directory.muduls.forms.features import backdrop

from lib import handler
 


async def features(call: types.CallbackQuery) -> None:
    keyboard = types.InlineKeyboardMarkup()
    keys = ["Фон","Текст","Подключить кнопку действия","Бэкграунд"]

    for i in keys:
        keyboard.add(types.InlineKeyboardButton(text = i,callback_data=i))
    await call.message.reply(text="Свойства",reply_markup=keyboard)




def register_handlers_features(dp: dispatcher):
    
    dp.register_callback_query_handler(features, Text(equals='Свойства'))
    backdrop.register_handlers_backdrop(dp)

    