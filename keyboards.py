import telebot
from config import COLOR_CHOICES, SIZE_CHOICES, FORMAT_CHOICES, BACK_COLOR_CHOICES

def get_color_buttons():
    markup = telebot.types.InlineKeyboardMarkup()
    for color, text in COLOR_CHOICES.items():
        btn = telebot.types.InlineKeyboardButton(text, callback_data=f"color_{color}")
        markup.add(btn)
    return markup

def get_back_color_buttons():
    markup = telebot.types.InlineKeyboardMarkup()
    for color, text in BACK_COLOR_CHOICES.items():
        markup.add(telebot.types.InlineKeyboardButton(text, callback_data=f"backcolor_{color}"))
    return markup

def get_size_buttons():
    markup = telebot.types.InlineKeyboardMarkup()
    for size in SIZE_CHOICES:
        btn = telebot.types.InlineKeyboardButton(size, callback_data=f"size_{size}")
        markup.add(btn)
    return markup

def get_format_buttons():
    markup = telebot.types.InlineKeyboardMarkup()
    for fmt in FORMAT_CHOICES:
        btn = telebot.types.InlineKeyboardButton(fmt, callback_data=f"format_{fmt}")
        markup.add(btn)
    return markup

def get_cancel_button():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("Отмена"))
    return markup