from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class MainMenuKeyboards:

    # К информации о добавке
    def main_menu(num):
        all_info = InlineKeyboardButton('ℹ️ Общая информация', callback_data=f'all_info_{num}')
        benefit = InlineKeyboardButton('❇️ Польза', callback_data=f'benefit_{num}')
        harm = InlineKeyboardButton('❗️ Вред', callback_data=f'harm_{num}')
        menu = InlineKeyboardMarkup().add(all_info); menu.row(benefit, harm)
        return menu

    # К общей информации о добавках
    def all_info_menu(num):
        benefit = InlineKeyboardButton('❇️ Польза', callback_data=f'benefit_{num}')
        harm = InlineKeyboardButton('❗️ Вред', callback_data=f'harm_{num}')
        main_menu = InlineKeyboardButton('🧪 О добавке', callback_data=f'main_menu_{num}')
        menu = InlineKeyboardMarkup().row(benefit, harm); menu.add(main_menu)
        return menu

    # К пользе добавок
    def benefit_menu(num):
        all_info = InlineKeyboardButton('ℹ️ Общая информация', callback_data=f'all_info_{num}')
        main_menu = InlineKeyboardButton('🧪 О добавке', callback_data=f'main_menu_{num}')
        harm = InlineKeyboardButton('❗️ Вред', callback_data=f'harm_{num}')
        menu = InlineKeyboardMarkup().add(all_info); menu.row(main_menu, harm)
        return menu

    # К вреду добавок
    def harm_menu(num):
        all_info = InlineKeyboardButton('ℹ️ Общая информация', callback_data=f'all_info_{num}')
        benefit = InlineKeyboardButton('❇️ Польза', callback_data=f'benefit_{num}')
        main_menu = InlineKeyboardButton('🧪 О добавке', callback_data=f'main_menu_{num}')
        menu = InlineKeyboardMarkup().add(all_info); menu.row(benefit, main_menu)
        return menu
