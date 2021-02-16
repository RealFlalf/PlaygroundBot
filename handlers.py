from app import bot, disp, ADMIN_ID

from aiogram.types import Message


async def send_to_admin(disp):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')


@disp.message_handler()
async def echo(message: Message):
    text = f'Твое сообщение: {message.text}'
    print(text)
    await message.answer(text=text)
