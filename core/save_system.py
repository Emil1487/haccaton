# core/save_system.py

import json
import os
from datetime import datetime

SAVE_PATH = "saves/"
SLOTS = ["slot_1.json", "slot_2.json", "slot_3.json"]
AUTO_SAVE = "auto.json"


class SaveSystem:

    @staticmethod
    def _get_path(slot):
        if slot == "auto":
            return os.path.join(SAVE_PATH, AUTO_SAVE)
        return os.path.join(SAVE_PATH, SLOTS[slot - 1])

    @staticmethod
    def save(slot, game_state):
        os.makedirs(SAVE_PATH, exist_ok=True)
        path = SaveSystem._get_path(slot)

        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "game_state": game_state
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load(slot):
        path = SaveSystem._get_path(slot)
        if not os.path.exists(path):
            return None

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)["game_state"]

    @staticmethod
    def auto_save(game_state):
        SaveSystem.save("auto", game_state)

    @staticmethod
    def get_save_info(slot):
        path = SaveSystem._get_path(slot)
        if not os.path.exists(path):
            return None

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return {
            "timestamp": data["timestamp"],
            "day": data["game_state"].get("day", 1),
            "resources": data["game_state"].get("resources", {})
        }

    @staticmethod
    def delete_save(slot):
        path = SaveSystem._get_path(slot)
        if os.path.exists(path):
            os.remove(path)
