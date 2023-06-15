from aiogram import types

from app.models import User
from app import utils


async def start_handler(message: types.Message):
    # Create a User object using the message.from_user data
    user = User(message.from_user)
    response = f'Hello {user.get_full_name()}'
    await utils.send_message_to_user(user.id, 'Let me think...')
    await message.reply(response)
