import logging
from my_bot.tg_bot import my_bot


async def send_message_to_user(user_id: int, message: str):
    bot = my_bot.bot
    try:
        await bot.send_message(chat_id=user_id, text=message)
    except Exception as e:
        logging.error(f"Failed to send message to user {user_id}: {str(e)}")
