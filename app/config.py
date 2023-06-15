from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")