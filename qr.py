from dotenv import load_dotenv
import os
import qrcode
import telebot

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

user_data = {}

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, f'Приветствую, {message.from_user.last_name} {message.from_user.first_name}! Я могу конвертировать информацию в QRcode')

@bot.message_handler(commands = ['qr'])
def qr(message):
    bot.send_message(message.chat.id, f'Напиши текст, который хочешь конвертировать в QRcode')
    user_data[message.chat.id] = True

@bot.message_handler(func=lambda message: user_data.get(message.chat.id))
def get_qr(message):
    data = message.text
    img = qrcode.make(data)
    img.save('qr-code.png')
    with open('qr-code.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)
    del user_data[message.chat.id]

bot.polling(none_stop = True)