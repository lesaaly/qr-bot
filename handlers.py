from config import COLOR_CHOICES, BACK_COLOR_CHOICES, SIZE_CHOICES, FORMAT_CHOICES
from keyboards import get_color_buttons, get_back_color_buttons, get_size_buttons, get_format_buttons, get_cancel_button
from qr_utils import generate_qr
from telebot import types

user_data = {}
qr_data = {}

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def main(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сгенерировать QR")
        btn2 = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2)
        bot.send_message(
            message.chat.id,
            f'Приветствую, {message.from_user.last_name} {message.from_user.first_name}! Я могу конвертировать информацию в QRcode',
            reply_markup=markup
        )

    @bot.message_handler(func=lambda m: m.text == "Сгенерировать QR")
    def qr(message):
        user_id = message.chat.id
        qr_data[user_id] = {}
        bot.send_message(user_id, "Выбери цвет QR-кода:", reply_markup=get_color_buttons())

    @bot.message_handler(func=lambda m: m.text == "Помощь")
    def help_message(message):
        bot.send_message(message.chat.id, "Этот бот генерирует QR-коды с разными цветами, фоном, размерами и форматами. Просто следуй шагам!")

    @bot.message_handler(func=lambda m: m.text == "Отмена")
    def cancel(message):
        user_id = message.chat.id
        user_data.pop(user_id, None)
        qr_data.pop(user_id, None)
        bot.send_message(user_id, "Процесс сброшен. Нажми 'Сгенерировать QR', чтобы начать заново.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        user_id = call.message.chat.id
        data = call.data

        if data.startswith("color_"):
            color = data.split("_")[1]
            qr_data[user_id]['color'] = color
            bot.send_message(user_id, "Выбери цвет фона QR-кода:", reply_markup=get_back_color_buttons())
            return

        if data.startswith("backcolor_"):
            back_color = data.split("_")[1]
            qr_data[user_id]['back_color'] = back_color
            bot.send_message(user_id, "Выбери размер (в пикселях):", reply_markup=get_size_buttons())
            return

        if data.startswith("size_"):
            size = int(data.split("_")[1])
            qr_data[user_id]['size'] = size
            bot.send_message(user_id, "Выбери формат:", reply_markup=get_format_buttons())
            return

        if data.startswith("format_"):
            fmt = data.split("_")[1]
            qr_data[user_id]['format'] = fmt
            bot.send_message(user_id, "Теперь напиши текст, который нужно конвертировать в QR-код", reply_markup=get_cancel_button())
            user_data[user_id] = True
            return

    @bot.message_handler(func=lambda message: user_data.get(message.chat.id))
    def get_qr(message):
        user_id = message.chat.id
        text = message.text.strip()
        if text.lower() == "отмена":
            user_data.pop(user_id, None)
            qr_data.pop(user_id, None)
            bot.send_message(user_id, "Процесс сброшен. Нажми 'Сгенерировать QR', чтобы начать заново.")
            return

        try:
            if not text:
                bot.send_message(user_id, "Текст не должен быть пустым! Попробуйте еще раз.")
                return

            color = qr_data.get(user_id, {}).get('color', 'black')
            back_color = qr_data.get(user_id, {}).get('back_color', 'white')
            size = qr_data.get(user_id, {}).get('size', 300)
            fmt = qr_data.get(user_id, {}).get('format', 'png')

            bio = generate_qr(text, fill_color=color, back_color=back_color, size=size, fmt=fmt)
            bot.send_photo(user_id, bio)
        except Exception as e:
            print(f"[ERROR] {e}")
            bot.send_message(user_id, "Ошибка при генерации QR-кода. Попробуйте еще раз.")
        finally:
            user_data.pop(user_id, None)
            qr_data.pop(user_id, None)