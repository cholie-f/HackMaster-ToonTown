from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN
from handlers.start import start
from handlers.hack import handle_hack_start, handle_pin_input
from services.gsheets import init_gsheets

def main():
    # Инициализация
    gsheets_client = init_gsheets()
    
    # Создаем updater и dispatcher
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    
    # Регистрируем обработчики
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("hack", handle_hack_start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_pin_input))
    
    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
