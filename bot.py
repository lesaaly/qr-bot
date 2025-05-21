from config import BOT_TOKEN
import telebot
from handlers import register_handlers

bot = telebot.TeleBot(BOT_TOKEN)
register_handlers(bot)

if __name__ == "__main__":
    bot.polling(none_stop=True)