import os

class Settings:
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    MAX_ATTEMPTS = 5

config = Settings()
