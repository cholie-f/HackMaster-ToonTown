import random
from telegram import Update
from telegram.ext import CallbackContext
from services.security import generate_pin, check_pin

def handle_hack_start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    state = context.user_data['state']
    
    state.current_pin = generate_pin()
    state.step = 'hacking'
    
    update.message.reply_text("[you start the party]\nВведите запрос в формате: запрос {система} {доступ} {информация}")

def handle_pin_input(update: Update, context: CallbackContext):
    user_pin = update.message.text
    state = context.user_data['state']
    
    result = check_pin(user_pin, state.current_pin, state.debug_mode)
    update.message.reply_text(result)
