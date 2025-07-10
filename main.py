from telegram.ext import ApplicationBuilder
import os

# Токен теперь берётся из переменных окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("Бот работает безопасно!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
import os

async def post_init(app):
    await app.bot.set_my_commands([
        ("start", "Начать взлом сейфа"),
        ("hack", "Попробовать подобрать код")
    ])

def main():
    app = ApplicationBuilder() \
        .token(os.getenv("TELEGRAM_TOKEN")) \
        .post_init(post_init) \
        .build()
    
    setup_handlers(app)
    app.run_polling()

if __name__ == "__main__":
    main()
