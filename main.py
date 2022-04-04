from config import dp, loop
from aiogram import executor
from commands.commands import *






if __name__ == '__main__':
    executor.start_polling(dp, loop=loop, skip_updates=True)