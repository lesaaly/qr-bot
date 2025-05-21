from dotenv import load_dotenv
import os
import qrcode
import telebot
import io

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

user_data = {}

qr_data = {}

COLOR_CHOICES = {
    "black": "Черный",
    "blue": "Синий",
    "red": "Красный"
}

SIZE_CHOICES = [200, 300, 400]

FORMAT_CHOICES = ["png", "jpeg"]

def get_color_buttons():
    markup = telebot.types.InlineKeyboardMarkup()
    for color, text in COLOR_CHOICES.items():
        btn = telebot.types.InlineKeyboardButton(text, callback_data=f"color_${color}")
        markup.add(btn)
    return markup

def get_size_buttons():
    markup = telebot.types.InlineKeyboardMarkup()
    for size, text in SIZE_CHOICES.items():
        btn = telebot.types.InlineKeyboardButton(text, callback_data=f"color_${size}")
        markup.add(btn)
    return markup

def get_format_buttons():
    markup = telebot.types.InlineKeyboardMarkup()
    for fmt, text in FORMAT_CHOICES.items():
        btn = telebot.types.InlineKeyboardButton(text, callback_data=f"color_${fmr}")
        markup.add(btn)
    return markup

def generate_qr(data, fill_color='black', back_color='white', size=300, fmt='PNG'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    img = img.resize((size, size))
    bio = io.BytesIO()
    img.save(bio, fmt.upper())
    bio.name = f'qr.{fmt.lower()}'
    bio.seek(0)
    return bio

@bot.message_handler(commands = ['start'])
def main(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Сгенерировать QR")
    btn2 = telebot.types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 
                     f'Приветствую, {message.from_user.last_name} {message.from_user.first_name}! Я могу конвертировать информацию в QRcode', 
                     reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Сгенерировать QR")
def qr(message):
    user_id = message.chat.id 
    qr_data[user_id] = {}
    bot.send_message(message.chat.id, "Выбери цвет QR-кода:", reply_markup=get_color_buttons())

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_id = call.message.chat.id
    data = call.data

    if data.startswith("color_"):
        color = data.split("_")[1]
        qr_data[user_id]['color'] = color
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
        bot.send_message(user_id, "Теперь напиши текст, который нужно конвертировать в QR-код")
        user_data[user_id] = True
        return

@bot.message_handler(func=lambda message: user_data.get(message.chat.id))
def get_qr(message):
    user_id = message.chat.id
    try: 
        data = message.text.strip()
        if not data:
            bot.send_message(message.chat.id, f"Текст не должен быть пустым! Попробуйте еще раз.")
            return
        color = qr_data.get(user_id, {}).get('color', 'black')
        size = qr_data.get(user_id, {}).get('size', 300)
        fmt = qr_data.get(user_id, {}).get('format', 'png')
        bio = generate_qr(data, fill_color=color, size=size, fmt=fmt)
        bot.send_photo(message.chat.id, bio)
    except Exception as e:
        print(f"[ERROR] {e}")
        bot.send_message(message.chat.id, "Ошибка при генерации QR-кода. Попробуйте еще раз.")
    finally:
        user_data.pop(user_id, None)
        qr_data.pop(user_id, None)

bot.polling(none_stop = True)