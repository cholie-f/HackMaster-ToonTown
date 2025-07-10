from telegram import ReplyKeyboardMarkup

def get_yes_no_keyboard():
    return ReplyKeyboardMarkup(
        [['Да', 'Нет']],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def get_pin_hints_keyboard():
    return ReplyKeyboardMarkup(
        [['1234', '0000'], ['2580', '1990']],
        resize_keyboard=True,
        one_time_keyboard=True
    )
