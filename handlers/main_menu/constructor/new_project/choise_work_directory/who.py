from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text

from handlers.main_menu.constructor.new_project.choise_work_directory.muduls.forms import registrate_forms

from lib import handler
 


async def practice(call: types.CallbackQuery) -> None:
    keyboard = types.InlineKeyboardMarkup()
    keys = ["Формы","Оформление","Социальные сети","Модуль управления"]
    for i in keys:
        keyboard.add(types.InlineKeyboardButton(text = i,callback_data=i))
    await call.message.reply(text="модули",reply_markup=keyboard)




def register_handlers(dp: dispatcher):
    
    dp.register_callback_query_handler(practice, Text(equals="Практис"))
    registrate_forms.register_handlers_forms(dp)
    