from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
import random
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

# Состояния диалога
AUTH, SAFE_CHOICE, PIN_ENTRY = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Начало диалога, запрос имени персонажа"""
    await update.message.reply_text(
        "🔒 ToonTown Security System\n"
        "Введите имя персонажа:",
        reply_markup=ReplyKeyboardRemove()
    )
    return AUTH

async def authenticate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Заглушка аутентификации"""
    context.user_data['character'] = {
        'name': update.message.text,
        'skill': 'Хакер',  # Заглушка
        'session_start': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    await update.message.reply_text(
        f"✅ Доступ разрешен: {update.message.text}\n"
        "Введите номер сейфа:",
        reply_markup=ReplyKeyboardRemove()
    )
    return SAFE_CHOICE

async def choose_safe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Обработка выбора сейфа с генерацией пин-кода"""
    safe_number = update.message.text
    
    # Генерируем случайный 4-значный пин-код
    context.user_data['safe'] = {
        'number': safe_number,
        'pin': ''.join(random.sample('0123456789', 4)),
        'level': 'easy',  # Заглушка уровня сложности
        'attempts_left': 5
    }
    
    character = context.user_data['character']
    await update.message.reply_text(
        f"👤 Пользователь: {character['name']}\n"
        f"🕒 Сессия начата: {character['session_start']}\n"
        f"⚡ Навык: {character['skill']}\n"
        f"🔓 Взлом сейфа: {safe_number}\n"
        f"📊 Уровень: Easy\n\n"
        "Введите 4-значный пин-код:",
        reply_markup=ReplyKeyboardRemove()
    )
    return PIN_ENTRY

async def hack_attempt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Проверка пин-кода"""
    user_input = update.message.text
    safe_data = context.user_data['safe']
    
    # Проверка формата
    if not (user_input.isdigit() and len(user_input) == 4):
        await update.message.reply_text("❌ Пин-код должен содержать ровно 4 цифры")
        return PIN_ENTRY
    
    safe_data['attempts_left'] -= 1
    
    if user_input == safe_data['pin']:
        await update.message.reply_text(
            "🎉 Сейф взломан!\n"
            "Доступ к документам получен.\n\n"
            "Для нового взлома введите /start",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    else:
        # Анализ попытки
        correct_digits = sum(d in safe_data['pin'] for d in user_input)
        correct_positions = sum(1 for i in range(4) if user_input[i] == safe_data['pin'][i])
        
        if safe_data['attempts_left'] <= 0:
            await update.message.reply_text(
                "🚨 Сейф заблокирован! Попытки исчерпаны.\n"
                "Для нового взлома введите /start",
                reply_markup=ReplyKeyboardRemove()
            )
            return ConversationHandler.END
        
        hint = (
            f"🔐 Неверный код! Осталось попыток: {safe_data['attempts_left']}\n"
            f"• Правильных цифр: {correct_digits}\n"
            f"• На своих местах: {correct_positions}"
        )
        await update.message.reply_text(hint)
        return PIN_ENTRY

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отмена диалога"""
    await update.message.reply_text("❌ Операция отменена")
    return ConversationHandler.END
