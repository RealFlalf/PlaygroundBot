from main import bot, disp, ADMIN_ID

from aiogram.types import Message

async def send_to_admin(disp):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')

if __name__ == '__main__':
    pass