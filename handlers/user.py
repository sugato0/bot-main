from aiogram import types, dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_user
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from lib import handler
import emoji
import re 

START_TEXT = """
<b>Вас приветсвует Телеграм Бот PRACTICE</b>
Начиная работу с ботом, <b>ВЫ даете согалсие на обработку персональных данных</b>
Чтобы начать регистрацию нажмите кнопку - <b>"Регистрация"</b>"""

CANCLE_TEXT = """
Чтобы начать регистрацию нажмите кнопку - <b>"Регистрация"</b>
"""

class ClientStates(StatesGroup):
    fio = State()
    telephone = State()
    date_of_birthday = State()
    education = State()
    profession = State()
    email = State()

async def start_registration(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id, 
                        photo='https://i.imgur.com/o7sOfGx.png', 
                        caption=START_TEXT, 
                        parse_mode='HTML', 
                        reply_markup=kb_user.get_keyboard())

async def choose(message: types.Message) -> None:
    await message.reply(text="Выберите тип регистрации", 
                        reply_markup=kb_user.choose_keyboard())
    
async def event(message: types.Message) -> None:
    await message.reply(text="Выберите мероприятие", 
                        reply_markup=kb_user.event_keyboard())

async def get_event(message: types.Message) -> None:
    await message.reply(text="Введите ваше ФИО", 
                        reply_markup=kb_user.cancle_keyboard())
    await ClientStates.fio.set()

async def reg(message: types.Message) -> None:
    await message.reply(text="Нажмите кнопку 'Регистрация'", 
                        reply_markup=kb_user.get_keyboard())

async def cancle(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply(text=CANCLE_TEXT, reply_markup=kb_user.get_keyboard(), parse_mode='HTML')
    await state.finish()

async def get_fio(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['fio'] = message.text
    await ClientStates.next() 
    await message.reply('Введите ваш телефон', reply_markup=kb_user.cancle_keyboard())

async def get_telephone(message: types.Message, state: FSMContext) -> None:
    phone = await handler.is_int_phone(message.text)
    if phone == True:
        async with state.proxy() as data:
            data['telephone'] = message.text
        await ClientStates.next() 
        await message.reply('Введите вашу дату рождения.\n<b>Формат: DD.MM.YYYY</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')
    else:
        await message.reply('Неверный ввод')

async def get_date_of_birthday(message: types.Message, state: FSMContext) -> None:
    date = await handler.is_valid_date(message.text)
    if date == True:
        async with state.proxy() as data:
            data['date_of_birthday'] = message.text
        await ClientStates.next() 
        await message.reply('Введите ваше учебное заведение', reply_markup=kb_user.cancle_keyboard())
    else:
        await message.reply('Неверный ввод.\n<b>Формат: DD.MM.YYYY</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')

async def get_education(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['education'] = message.text
    await ClientStates.next() 
    await message.reply('Введите вашу специальность', reply_markup=kb_user.cancle_keyboard())

async def get_profession(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['profession'] = message.text
    await ClientStates.next() 
    await message.reply('Введите ваш email.\n<b>Формат: practice@gmail.com</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')

async def get_email(message: types.Message, state: FSMContext) -> None:
    check = await handler.is_valid_email(message.text)
    if check == True:
        async with state.proxy() as data:
            data['email'] = message.text
        async with state.proxy() as data:
            await bot.send_message(chat_id=message.from_user.id,
                                text=f"ФИО: {data['fio']}\nТелефон: {data['telephone']}\nДата рождения: {data['date_of_birthday']}\nУчебное учреждение: {data['education']}\nСпециальность: {data['profession']}\nЭл. почта: {data['email']}")
        await state.finish()  
    else:
        await message.reply('Неверный ввод.\n<b>Формат: practice@gmail.com</b>', reply_markup=kb_user.cancle_keyboard(), parse_mode='HTML')
    await message.answer('Ваши данные сохранены', reply_markup=kb_user.choose_keyboard())


async def want_to_practice(message: types.Message) -> None:
    await message.reply(text='Выберите кнопку', reply_markup=kb_user.want_to_team())

async def alexander(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id, 
                        photo='https://i.imgur.com/oC9qlF0.jpeg',
                        caption="Чтобы попасть в команду, напишите Александру Трошкину", 
                        reply_markup=kb_user.link())    
    await bot.send_message(chat_id=message.from_user.id, text=emoji.emojize("👆"), reply_markup=kb_user.choose_keyboard())

async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id)

def register_handlers_user(dp: dispatcher):
    dp.register_message_handler(start_registration, commands=["start"])
    dp.register_message_handler(choose, Text(equals='Регистрация'))
    dp.register_message_handler(cancle, Text(equals='Вернуться обратно'), state='*')
    dp.register_message_handler(event, Text(equals='Мероприятия'))
    dp.register_message_handler(get_event, Text(['Интенсив ПРАКТИС', 'КОД ИБ + ПРАКТИС']))
    dp.register_message_handler(get_fio, state=ClientStates.fio)
    dp.register_message_handler(get_telephone, state=ClientStates.telephone)
    dp.register_message_handler(get_date_of_birthday, state=ClientStates.date_of_birthday)
    dp.register_message_handler(get_education, state=ClientStates.education)
    dp.register_message_handler(get_profession, state=ClientStates.profession)
    dp.register_message_handler(get_email, state=ClientStates.email)
    dp.register_message_handler(want_to_practice, Text(equals='Что такое PRACTICE?'))
    dp.register_message_handler(alexander, Text(equals='Хочу в команду'))
    dp.register_callback_query_handler(lambda c: c.data == 'link')
