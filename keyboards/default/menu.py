from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup()
keys = [
    InlineKeyboardButton(text='Время пожеланий', callback_data='menu_time_to'),
    InlineKeyboardButton(text='Прямо сейчас', callback_data='menu_time_now')
]
for key in keys:
    main_menu.add(key)
