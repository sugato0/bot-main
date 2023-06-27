from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text

from handlers.main_menu.constructor.new_project.choise_work_directory.muduls.forms.features import registrate_features

from lib import handler
 


async def forms(call: types.CallbackQuery) -> None:
    keyboard = types.InlineKeyboardMarkup()
    keys = ["Типирование","Свойства","Выбор модуля","Работа с формами"]

    for i in keys:
        keyboard.add(types.InlineKeyboardButton(text = i,callback_data=i))
    await call.message.reply(text="формы",reply_markup=keyboard)




def register_handlers_forms(dp: dispatcher):
    
    dp.register_callback_query_handler(forms, Text(equals='Формы'))
    registrate_features.register_handlers_features(dp)

    