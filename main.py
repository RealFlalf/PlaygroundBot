import asyncio
from aiogram import Bot, Dispatcher, executor


BOT_TOKEN = '1604493422:AAF0uumNzRdAPe9BWZi5tx25ux1kEgWYg50'
ADMIN_ID = '344622313'

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
disp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import send_to_admin
    executor.start_polling(disp, on_startup=send_to_admin)