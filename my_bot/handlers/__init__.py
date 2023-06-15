from . import message_handler, callback_handler
from my_bot.tg_bot import my_bot
print("init")

my_bot.dp.register_message_handler(message_handler.start_handler, commands=['start'])


my_bot.dp.register_callback_query_handler(callback_handler.handle_callback)
