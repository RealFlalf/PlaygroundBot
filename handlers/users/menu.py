from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('ВЫбери что хочешь сделать', reply_markup=menu)


@dp.message_handler(Text(equals=['Время', 'Пожелание']))
async def send_time(message: Message):
    await message.answer(f'Время: {message.text}', reply_markup=ReplyKeyboardRemove())
