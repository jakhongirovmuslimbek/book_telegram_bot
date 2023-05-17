
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from sqlite_functions import *
from buttons import *

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# create baza
create_db()
create_table_users()

create_table_category()
create_table_books()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    telegram_id = message.from_user.id
    user = select_users(telegram_id)
    if user is None:
        await message.reply("Telefon raqamingizni yuboring!", reply_markup=phone_number)
    else:
        await message.reply("Siz bazada mavjudsiz!")
        await message.answer("Marhamat menu: ", reply_markup=main_menu)


@dp.message_handler(content_types='contact')
async def echo(message: types.Message):
    username = message.from_user.username
    telegram_id = message.from_user.id
    phone_number = message.contact['phone_number']
    insert_users(username, telegram_id, phone_number)
    await message.answer("Siz ro'yxatdan o'tdingiz!")
    await message.answer("Marhamat menu: ", reply_markup=main_menu)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)