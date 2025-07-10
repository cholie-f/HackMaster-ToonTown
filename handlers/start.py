from telegram import Update
from telegram.ext import CallbackContext
from models.user_state import UserState

USER_STATES = {}

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    USER_STATES[user_id] = UserState()
    USER_STATES[user_id].step = 'awaiting_name'
    update.message.reply_text("ToonTown Security System\nВведите имя персонажа:")
