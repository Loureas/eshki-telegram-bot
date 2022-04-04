import logging, asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)


API_TOKEN = ''  # Здесь должен быть API токен вашего бота, полученный в @BotFather


loop = asyncio.get_event_loop()
bot = Bot(API_TOKEN, loop)
dp = Dispatcher(bot, loop, MemoryStorage())
