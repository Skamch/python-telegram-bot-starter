# Telegram Simple Bot Starter Template with aiogram

This is a starter template for building Telegram bots using the aiogram library. It provides a basic structure and examples to help you get started quickly with developing your own Telegram bot.


- `my_bot/`: The main package of your bot.
  - `my_bot/__init__.py`: Package initialization file.
  - `my_bot/handlers/`: Package for message and callback handlers of your bot.
    - `my_bot/handlers/__init__.py`: Package initialization file for handlers.
    - `my_bot/handlers/message_handler.py`: Module with message handlers for your bot.
    - `my_bot/handlers/callback_handler.py`: Module with callback handlers for your bot.
  - `my_bot/models/`: Package for data models of your bot.
    - `my_bot/models/__init__.py`: Package initialization file for models.
    - `my_bot/models/user.py`: Module with the user model for your bot.
  - `my_bot/utils/`: Package for utility functions of your bot.
    - `my_bot/utils/__init__.py`: Package initialization file for utilities.
    - `my_bot/utils/helpers.py`: Module with helper functions for your bot.
  - `my_bot/__main__.py`: The main module of your bot, where you create and configure the bot instance.
  - `my_bot/config.py`: Module with configuration parameters for your bot.
  - `my_bot/tg_bot.py`:This module initializes and runs a Telegram bot using the aiogram library, allowing it to receive and respond to messages from users on the Telegram platform.

- `data/`: Folder for storing data of your bot, such as text files, images, and other resources.

- `requirements.txt`: File containing the list of dependencies for your Python project.

- `Dockerfile`: File for creating a Docker image of your bot, if you plan to use Docker.



## Features

- Basic bot structure with an example command and message handler
- Integration with aiogram library for easy interaction with the Telegram Bot API
- Modular design with separate packages for handlers and utilities
- Docker support for containerization and easy deployment

## Prerequisites

- Python 3.7+
- Telegram Bot Token (obtained from BotFather)
- Docker (optional, for containerization)

## Getting Started

1. Clone this repository:
   ```shell
   git clone https://github.com/Skamch/telegram-bot-starter.git
2. Update the [config.env](config.env) with your Telegram Bot Token:
   ```
   TELEGRAM_BOT_TOKEN = 'your_bot_token'
3. Run Bot
    ```shell
   bash start

## Licence 
```
MIT License

Copyright 2023 Kiryl Volkau

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the telegram-bot-starter), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

