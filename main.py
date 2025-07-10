#!/usr/bin/env python3
# main.py - Точка входа для бота "Взлом сейфа"
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler
)
from bot.handlers import (
    start,
    authenticate,
    choose_safe,
    hack_attempt,
    cancel,
    AUTH,
    SAFE_CHOICE,
    PIN_ENTRY
)
from config.settings import config
import logging
import os

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'  # Логи будут сохраняться в файл
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Инициализация бота
        application = ApplicationBuilder() \
            .token(config.TOKEN) \
            .post_init(post_init) \
            .build()

        # Настройка обработчиков
        setup_handlers(application)

        logger.info("Бот запускается...")
        application.run_polling()

    except Exception as e:
        logger.error(f"Ошибка запуска бота: {e}", exc_info=True)

async def post_init(application):
    """Действия после инициализации бота"""
    await application.bot.set_my_commands([
        ('start', 'Начать игру "Взлом сейфа"'),
        ('help', 'Помощь по игре'),
        ('cancel', 'Отменить текущее действие')
    ])
    logger.info("Команды бота обновлены")

def setup_handlers(app):
    """Регистрация всех обработчиков команд"""
    # Основной обработчик диалога
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            AUTH: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    authenticate
                )
            ],
            SAFE_CHOICE: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    choose_safe
                )
            ],
            PIN_ENTRY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    hack_attempt
                )
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        allow_reentry=True
    )

    # Регистрируем обработчики
    app.add_handler(conv_handler)
    
    # Обработчик ошибок
    app.add_error_handler(error_handler)

async def error_handler(update, context):
    """Обработчик ошибок"""
    logger.error(f"Ошибка: {context.error}", exc_info=True)
    if update:
        await update.message.reply_text("⚠️ Произошла ошибка. Попробуйте позже.")

if __name__ == '__main__':
    # Проверка наличия токена
    if not config.TOKEN:
        logger.critical("Токен бота не найден!")
        print("ОШИБКА: Задайте TELEGRAM_TOKEN в config/settings.py или .env")
        exit(1)
    
    main()
