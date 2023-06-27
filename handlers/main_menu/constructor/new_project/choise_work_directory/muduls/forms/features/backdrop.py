from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from lib import handler
from requests import get,post,delete
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
req = "background"
answer = str(server)+req

class Enter(StatesGroup):
    color = State()
    image = State()
    video = State()
    link = State()
    text = State()


async def backdrop(call: types.CallbackQuery) -> None:
    keyboard = types.InlineKeyboardMarkup()
    keys = ["Узнать параметры","Удалить задний фон","Цвет заднего фона","Изображение на заднем фоне","Видео на заднем фоне","Ссылка на заднем фоне","Текст на заднем фоне"]
    for i in keys:
        keyboard.add(types.InlineKeyboardButton(text = i,callback_data=i))
    await call.message.reply(text="Параметры фона",reply_markup=keyboard)

async def getBackdrop(call: types.CallbackQuery) -> None:
    url = answer+"/"
    try:

        key = get(url)
        await call.message.reply(text=f"Параметры фона\n{key}")
    except:
        await call.message.reply(text=f"Что-то пошло не так, не удалось узнать параметры фона")

    



async def deleteBackdrop(call: types.CallbackQuery) -> None:
    url = answer+"/"
    try:

        delete(url)
        await call.message.reply(text=f"Фон успешно удален")
    except:
        await call.message.reply(text=f"Что-то пошло не так, фон не был удален")

    
async def postColorBackdrop(call: types.CallbackQuery,state: FSMContext) -> None:
    await Enter.color.set()
async def postColorBackdropST(message: types.Message,state: FSMContext) -> None:
    
    url = answer+"/color"


    try:

        post(url, data={"color":message.text})
        await message.reply(text=f"Цвет успешно изменен")
    except:
        await message.reply(text=f"Что-то пошло не так, цвет не был удален")

    await state.finish()

async def postImgBackdrop(call: types.CallbackQuery,state: FSMContext) -> None:
    await Enter.image.set()
async def postImgBackdropST(message: types.Message,state: FSMContext) -> None:
    
    url = answer+"/image"


    try:

        post(url, data={"url":message.text})
        await message.reply(text=f"Изображение успешно изменено")
    except:
        await message.reply(text=f"Что-то пошло не так, изображение не было сохранено")

    await state.finish()


async def postVideoBackdrop(call: types.CallbackQuery,state: FSMContext) -> None:
    await Enter.video.set()
async def postVideoBackdropST(message: types.Message,state: FSMContext) -> None:
    
    url = answer+"/video"


    try:

        post(url, data={"url":message.text})
        await message.reply(text=f"Видео успешно изменено")
    except:
        await message.reply(text=f"Что-то пошло не так, видео не было сохранено")

    await state.finish()

async def postLinkBackdrop(call: types.CallbackQuery,state: FSMContext) -> None:
    await Enter.link.set()
async def postLinkBackdropST(message: types.Message,state: FSMContext) -> None:
    
    url = answer+"/link"


    try:

        post(url, data={"url":message.text})
        await message.reply(text=f"Ссылка успешно добавлена")
    except:
        await message.reply(text=f"Что-то пошло не так, ссылка не была сохранена")

    await state.finish()

async def postTextBackdrop(call: types.CallbackQuery,state: FSMContext) -> None:
    await Enter.link.set()
async def postTextBackdropST(message: types.Message,state: FSMContext) -> None:
    
    url = answer+"/text"


    try:

        post(url, data={"url":message.text})
        await message.reply(text=f"Текст успешно добавлен")
    except:
        await message.reply(text=f"Что-то пошло не так, текст не был сохранён")

    await state.finish()




def register_handlers_backdrop(dp: dispatcher):
    
    dp.register_callback_query_handler(backdrop, Text(equals='Фон'))

    dp.register_callback_query_handler(getBackdrop, Text(equals='Узнать параметры'))
    dp.register_callback_query_handler(deleteBackdrop, Text(equals='Удалить задний фон'))

    dp.register_callback_query_handler(postColorBackdrop, Text(equals='Цвет заднего фона'))
    dp.register_message_handler(postColorBackdropST, state = Enter.color)
    
    dp.register_callback_query_handler(postImgBackdrop, Text(equals='Изображение на заднем фоне'))
    dp.register_message_handler(postImgBackdropST, state = Enter.image)

    dp.register_callback_query_handler(postVideoBackdrop, Text(equals='Видео на заднем фоне'))
    dp.register_message_handler(postVideoBackdropST, state = Enter.video)

    dp.register_callback_query_handler(postLinkBackdrop, Text(equals='Ссылка на заднем фоне'))
    dp.register_message_handler(postLinkBackdropST, state = Enter.link)

    dp.register_callback_query_handler(postTextBackdrop, Text(equals='Текст на заднем фоне'))
    dp.register_message_handler(postTextBackdropST, state = Enter.text)

