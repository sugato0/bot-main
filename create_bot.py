import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
storage=MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot,
                storage=storage)