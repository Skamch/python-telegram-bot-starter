from aiogram import types


async def handle_callback(callback_query: types.CallbackQuery):
    # Extract the callback data from the callback query
    callback_data = callback_query.data

    # Handle the callback based on the callback data
    if callback_data == "option1":
        response_text = "You selected option 1."
    elif callback_data == "option2":
        response_text = "You selected option 2."
    else:
        response_text = "Invalid option selected."

    # Send the response
    await callback_query.message.answer(response_text)
