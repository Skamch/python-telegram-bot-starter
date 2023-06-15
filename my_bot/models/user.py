from aiogram.types import User as TelegramUser


class User:
    def __init__(self, telegram_user: TelegramUser):
        self.id = telegram_user.id
        self.username = telegram_user.username
        self.first_name = telegram_user.first_name
        self.last_name = telegram_user.last_name

    def get_full_name(self) -> str:
        """Returns the full name of the user."""
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name

    def __str__(self) -> str:
        """Returns a string representation of the user."""
        return f"User ID: {self.id}, Username: {self.username}, Name: {self.get_full_name()}"