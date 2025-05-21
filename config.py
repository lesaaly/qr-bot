import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

COLOR_CHOICES = {
    "black": "Черный",
    "blue": "Синий",
    "red": "Красный"
}

BACK_COLOR_CHOICES = {
    "white": "Белый",
    "yellow": "Жёлтый",
    "green": "Зелёный"
}

SIZE_CHOICES = [200, 300, 400]

FORMAT_CHOICES = ["png", "jpeg"]