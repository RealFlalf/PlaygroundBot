from loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.default import main_menu
from aiogram.dispatcher.filters import Command
from datetime import datetime


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('ВЫбери что хочешь сделать', reply_markup=main_menu)


@dp.callback_query_handler(text_contains='menu_')
async def send_time(call: CallbackQuery):
    time = datetime.now()
    await call.message.answer(f'Время: {time}', reply_markup=main_menu)
