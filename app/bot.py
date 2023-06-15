from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import config


class _TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())

    def run(self):
        executor.start_polling(self.dp)


telegram_bot = _TelegramBot(config.TELEGRAM_BOT_TOKEN)