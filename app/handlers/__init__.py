from . import message_handler, callback_handler
from app.bot import telegram_bot

telegram_bot.dp.register_message_handler(message_handler.start_handler, commands=['start'])


telegram_bot.dp.register_callback_query_handler(callback_handler.handle_callback)
