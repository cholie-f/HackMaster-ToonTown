class UserState:
    def __init__(self):
        self.step = None
        self.character_name = None
        self.skill = None
        self.safe_number = None
        self.current_pin = None
        self.attempts = 0
        self.debug_mode = False
        self.access_level = None
        self.timer = 100
        self.request_info = None
