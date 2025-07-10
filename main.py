from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from bot.handlers import start, authenticate, choose_safe, hack_attempt, cancel, AUTH, SAFE_CHOICE, PIN_ENTRY
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    application = ApplicationBuilder().token("ВАШ_ТОКЕН").build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            AUTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, authenticate)],
            SAFE_CHOICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_safe)],
            PIN_ENTRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, hack_attempt)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
