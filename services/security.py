def generate_pin():
    return ''.join(random.sample('0123456789', 4))

def check_pin(user_pin, correct_pin, debug_mode=False):
    if user_pin == correct_pin:
        return "Доступ разрешен!"
    
    if debug_mode:
        correct_digits = len(set(user_pin) & set(correct_pin))
        wrong_digits = 4 - correct_digits
        correct_positions = sum(1 for i in range(4) if user_pin[i] == correct_pin[i])
        
        return (f"Debug:\n"
                f"Неправильных цифр: {wrong_digits}\n"
                f"Правильные цифры на неверных позициях: {correct_digits - correct_positions}")
    
    return "Неверный PIN-код"
