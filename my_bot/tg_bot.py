import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from my_bot import config


class _TgBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())

    def run(self):
        executor.start_polling(self.dp)


my_bot = _TgBot(config.TELEGRAM_BOT_TOKEN)