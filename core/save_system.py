import json

class SaveSystem:

    @staticmethod
    def save(game_manager, filename="save.json"):
        data = game_manager.__dict__
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load(game_manager, filename="save.json"):
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
        game_manager.__dict__.update(data)
