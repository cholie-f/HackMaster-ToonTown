from datetime import datetime, timedelta

class SafeHackingSystem:
    def __init__(self, safe_info: dict):
        self.correct_pin = "1234"  # Заглушка, замените на реальный код
        self.attempts = 0
        self.max_attempts = 5
        self.level = safe_info['level']
        self.timer = None
        
        if self.level in ['medium', 'hard']:
            self.timer = datetime.now() + timedelta(minutes=int(safe_info['timer']))
    
    def get_remaining_time(self) -> str:
        if not self.timer:
            return "∞"
        remaining = self.timer - datetime.now()
        return f"{remaining.seconds//60}:{remaining.seconds%60:02d}"
    
    def check_timeout(self) -> bool:
        return self.timer and datetime.now() > self.timer
