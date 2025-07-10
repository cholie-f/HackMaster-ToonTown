import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class GoogleSheetsClient:
    def __init__(self, creds_file: str):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        self.client = gspread.authorize(creds)

    def get_character(self, sheet_id: str, name: str) -> dict:
        """Получает данные персонажа"""
        try:
            sheet = self.client.open_by_key(sheet_id).worksheet("Персонажи")
            records = sheet.get_all_records()
            for record in records:
                if record['Название'].lower() == name.lower():
                    return {
                        'name': record['Название'],
                        'skill': record['Навык'],
                        'session_start': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
            return None
        except Exception as e:
            logger.error(f"Ошибка получения персонажа: {str(e)}")
            return None

    def get_safe_info(self, sheet_id: str, safe_number: str) -> dict:
        """Получает данные сейфа"""
        try:
            sheet = self.client.open_by_key(sheet_id).worksheet("Сейфы")
            records = sheet.get_all_records()
            for record in records:
                if record['Номер'].lower() == safe_number.lower():
                    return {
                        'number': record['Номер'],
                        'level': record['Уровень'],
                        'timer': record['Таймер']  # В минутах
                    }
            return None
        except Exception as e:
            logger.error(f"Ошибка получения сейфа: {str(e)}")
            return None
