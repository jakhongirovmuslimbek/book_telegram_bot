
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from sqlite_functions import *

phone_number = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("📞 Telefon raqam yuborish!", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("Main menu!")
        ]
    ],
    resize_keyboard=True
)

def select_category_button():
    data = select_category()
    button = InlineKeyboardMarkup(row_width=2)
    for i in data:
        button.insert(InlineKeyboardButton(text=i[1], callback_data=f"category_{i[0]}"))
    return button    

def select_books_categor_id_button(category_id):
    data = select_by_category_id(category_id)
    button = InlineKeyboardMarkup(row_width=2)
    for i in data:
        button.insert(InlineKeyboardButton(text=i[2], callback_data=f"books_{i[0]}"))
    return button    
       

