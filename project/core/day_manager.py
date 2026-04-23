import json
import os
from config import DATA_DIR

class DayManager:
    """Загружает расписание NPC по дням"""

    def __init__(self):
        with open(os.path.join(DATA_DIR, "days.json"), encoding="utf-8") as f:
            self.days_data = json.load(f)

    def get_characters_for_day(self, day_number):
        return self.days_data.get(str(day_number), [])
