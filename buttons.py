
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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