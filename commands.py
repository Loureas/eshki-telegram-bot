import requests
from aiogram import types
from config import dp, bot
from bs4 import BeautifulSoup
from keyboards import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("""
Привет!
С помощью меня ты можешь узнать информацию о пищевых добавках 🧪

Отправь мне номер пищевой добавки и я пришлю информацию о ней.
""")


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def pars(message: types.Message):
    try:
        if int(message.text):
            URL = f'https://dobavkam.net/additives/e{message.text}'
            page = requests.get(URL)
            page = BeautifulSoup(page.text, 'lxml')
            try:
                # Происхождение
                item = page.find('div', class_='addheader__right-top')
                text = item.text.split('\n')
                origins = ''; n = 0
                for i in text:
                    if i != '':
                        if n == 0:
                            origins += i[0:-14].lower()
                        else:
                            origins += ', ' + i[0:-14].lower()
                        n += 1

                # Опасность
                danger = page.find('div', class_='addprop--danger')
                danger = danger.text.strip()[0:-9].lower()

                # Категория
                category = page.find('div', class_='addprop--category')
                category = category.text.strip().lower()

                menu = MainMenuKeyboards.main_menu(message.text)
                await message.answer(f"""
🧪 Добавка: E{message.text}

🗂 Категория: {category}
🌱 Происхождение: {origins}
⚠️ Опасность: {danger}
""", reply_markup=menu)
            except AttributeError:
                await message.answer(f'Добавка {message.text} не найдена.')
    except ValueError:
        await message.answer('Чтобы получить информацию о добавке, отправь мне её номер.')



class Buttons:

    # Общая информация
    @dp.callback_query_handler(lambda c: c.data[0:8] == 'all_info')
    async def all_info_button(callback_query: types.CallbackQuery):
        num = callback_query.data.split('_')[2]
        URL = f'https://dobavkam.net/additives/e{num}'
        page = requests.get(URL)
        page = BeautifulSoup(page.text, 'lxml')
        info = page.find('div', class_='field field--block field--additive-info')
        all_info = info.text.split('Влияние на организм')
        menu = MainMenuKeyboards.all_info_menu(num)
        await bot.answer_callback_query(callback_query.id)
        await bot.edit_message_text(all_info[0], callback_query.from_user.id, callback_query.message.message_id, reply_markup=menu)

    # Польза
    @dp.callback_query_handler(lambda c: c.data[0:7] == 'benefit')
    async def benefit_button(callback_query: types.CallbackQuery):
        num = callback_query.data.split('_')[1]
        URL = f'https://dobavkam.net/additives/e{num}'
        page = requests.get(URL)
        page = BeautifulSoup(page.text, 'lxml')
        info = page.find('div', class_='field field--block field--additive-info')
        try:
            all_info = info.text.split('Вред')[0]
            benefit = all_info.split('Польза')[1]
            menu = MainMenuKeyboards.benefit_menu(num)
        except:
            try:
                all_info = info.text.split('Использование')[0]
                benefit = all_info.split('Польза')[1]
            except:
                benefit = 'Информация отсутствует.'
        menu = MainMenuKeyboards.benefit_menu(num)
        await bot.answer_callback_query(callback_query.id)
        await bot.edit_message_text(benefit, callback_query.from_user.id, callback_query.message.message_id, reply_markup=menu)

    # Вред
    @dp.callback_query_handler(lambda c: c.data[0:4] == 'harm')
    async def benefit_button(callback_query: types.CallbackQuery):
        num = callback_query.data.split('_')[1]
        URL = f'https://dobavkam.net/additives/e{num}'
        page = requests.get(URL)
        page = BeautifulSoup(page.text, 'lxml')
        info = page.find('div', class_='field field--block field--additive-info')
        try:
            all_info = info.text.split('Использование')[0]
            harm = all_info.split('Вред')[1]
        except:
            try:
                all_info = info.text.split('Польза')[0]
                harm = all_info.split('Вред')[1]
            except:
                harm = 'Информация отсутствует.'
        menu = MainMenuKeyboards.harm_menu(num)
        await bot.answer_callback_query(callback_query.id)
        await bot.edit_message_text(harm, callback_query.from_user.id, callback_query.message.message_id, reply_markup=menu)

    # О добавке
    @dp.callback_query_handler(lambda c: c.data[0:9] == 'main_menu')
    async def back_supple(callback_query: types.CallbackQuery):
        num = callback_query.data.split('_')[2]
        URL = f'https://dobavkam.net/additives/e{num}'
        page = requests.get(URL)
        page = BeautifulSoup(page.text, 'lxml')

        # Происхождение
        item = page.find('div', class_='addheader__right-top')
        text = item.text.split('\n')
        origins = ''; n = 0
        for i in text:
            if i != '':
                if n == 0:
                    origins += i[0:-14].lower()
                else:
                    origins += ', ' + i[0:-14].lower()
                n += 1

        # Опасность
        danger = page.find('div', class_='addprop--danger')
        danger = danger.text.strip()[0:-9].lower()

        # Категория
        category = page.find('div', class_='addprop--category')
        category = category.text.strip().lower()

        menu = MainMenuKeyboards.main_menu(num)
        await bot.edit_message_text(f"""
🧪 Добавка: E{num}

🗂 Категория: {category}
🌱 Происхождение: {origins}
⚠️ Опасность: {danger}
""", callback_query.from_user.id, callback_query.message.message_id, reply_markup=menu)


