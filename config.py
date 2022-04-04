import logging, asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)


API_TOKEN = '5205628852:AAFVsMoghJvy8ismvif5Dgf2QkPVzN-n1q0'


loop = asyncio.get_event_loop()
bot = Bot(API_TOKEN, loop)
dp = Dispatcher(bot, loop, MemoryStorage())
