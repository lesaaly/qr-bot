# QR Code Telegram Bot

Telegram-бот для генерации QR-кодов из любого текста.

## Описание

Этот бот позволяет пользователю отправить текстовое сообщение и получить в ответ QR-код с этим текстом.  
Бот написан на Python с использованием библиотек `telebot` и `qrcode`.

## Быстрый старт

1. **Клонируй репозиторий:**
    ```bash
    git clone https://github.com/lesaaly/qr-bot.git
    cd qr-bot
    ```

2. **Установи зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Создай файл `.env` в корне проекта и вставь свой токен:**
    ```
    BOT_TOKEN=ваш_токен_от_BotFather
    ```

4. **Запусти бота:**
    ```bash
    python bot.py
    ```

## Использование

- `/start` — получить приветственное сообщение.
- `/qr` — начать генерацию QR-кода. После этой команды отправь текст, который нужно закодировать.

## Зависимости

- [pyTelegramBotAPI (telebot)](https://pypi.org/project/pyTelegramBotAPI/)
- [qrcode](https://pypi.org/project/qrcode/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Pillow](https://pypi.org/project/Pillow/)

## Безопасность

**Никогда не загружай свой `.env` файл в публичные репозитории!**  
Токен должен храниться только локально.

---

Feel free to contribute, fork, or open issues!
# qr-bot
