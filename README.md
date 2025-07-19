# QR Code Telegram Bot

Telegram-бот для генерации QR-кодов с кастомными параметрами (цвет, фон, размер, формат).

## Фичи

- Генерация QR-кода из текста
- Выбор цвета QR и цвета фона
- Выбор размера и формата (PNG, JPEG)
- Интуитивные кнопки для каждого этапа
- Возможность отменить процесс на любом этапе

## Быстрый старт

1. **Клонируй репозиторий**
    ```bash
    git clone https://github.com/yourusername/qr-bot.git
    cd qr-bot
    ```

2. **Установи зависимости**
    ```bash
    pip install -r requirements.txt
    ```

3. **Создай файл `.env` и вставь токен бота**
    ```
    BOT_TOKEN=ваш_токен_от_BotFather
    ```

4. **Запусти бота**
    ```bash
    python bot.py
    ```

## Использование

- Нажми **Сгенерировать QR**
- Выбери цвет, цвет фона, размер, формат
- Введи текст — получи свой кастомный QR-код!
- Если что-то пошло не так — жми **Отмена**

## Зависимости

- [pyTelegramBotAPI (telebot)](https://pypi.org/project/pyTelegramBotAPI/)
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Советы по безопасности

- **Никогда не коммить файл `.env`** (добавь его в `.gitignore`).
- Токен хранить только локально.

---
