
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from sqlite_functions import *
from buttons import *
from aiogram.dispatcher.filters import Text

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
    user = select_users(telegram_id)
    if user is None:
        insert_users(username, telegram_id, phone_number)
        await message.answer("Siz ro'yxatdan o'tdingiz!")
        await message.answer("Marhamat menu: ", reply_markup=main_menu)
    else:
        await message.reply("888")    


# photo_handler
@dp.message_handler(content_types='photo')
async def echo(message: types.Message):
    print(
        message.photo[-1]['file_id']
    )

# Main menu!
@dp.message_handler(text='Main menu!')
async def echo(message: types.Message):
    info = select_category_button()
    await message.answer("Bo'limlardan  birini tanglang...", reply_markup=info)

@dp.callback_query_handler(Text(startswith='category_'))
async def echo(call: types.CallbackQuery):
    index = call.data.index("_")
    category_id = call.data[index+1:]
    info_1 = select_books_categor_id_button(category_id)
    await call.message.answer("Kitoblardan  birini tanglang...", reply_markup=info_1)

@dp.callback_query_handler(Text(startswith='books_'))
async def echo(call: types.CallbackQuery):
    index = call.data.index("_")
    id = call.data[index+1:]
    info_2 = select_book_by_id(id)
    await bot.send_photo(chat_id=call.from_user.id, photo=info_2[4], caption=f"Kitob nomi:  {info_2[2]}\n\n{info_2[3]}") 
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)