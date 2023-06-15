from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
PIXABAY_TOKEN = getenv("PIXABAY_TOKEN")
