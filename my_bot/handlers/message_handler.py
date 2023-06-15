from my_bot import my_bot
from aiogram import types


@my_bot.dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_full_name = message.from_user.full_name

    response = f'Hello {user_full_name}'

    await message.reply(response)
