import logging
from app.bot import telegram_bot


async def send_message_to_user(user_id: int, message: str):
    bot = telegram_bot.bot
    try:
        await bot.send_message(chat_id=user_id, text=message)
    except Exception as e:
        logging.error(f"Failed to send message to user {user_id}: {str(e)}")
