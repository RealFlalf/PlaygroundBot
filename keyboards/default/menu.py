from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Время')
        ],
        [
            KeyboardButton(text='Прислать сообщене')
        ]
    ],
    resize_keyboard=True
)