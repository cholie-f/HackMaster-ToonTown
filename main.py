from telegram.ext import ApplicationBuilder, CommandHandler
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update, context):
    await update.message.reply_text("🛡️ Бот успешно запущен!")

def is_valid_token(token: str) -> bool:
    return (token and 
            len(token) > 30 and 
            ":" in token and 
            not any(word in token.lower() for word in ["ваш", "token", "пример"]))

def main():
    TOKEN = "7781651048:AAGTycZs55gVorv9uOTtT7gTd9jFamznm_8"  # ← Вставьте СВОЙ токен
    
    if not is_valid_token(TOKEN):
        print("ОШИБКА: Неверный токен! Получите через @BotFather")
        return
    
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        logging.info("Запуск бота...")
        app.run_polling()
    except Exception as e:
        logging.error(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    main()
