class GameManager:
    """Управляет глобальными ресурсами игры"""

    def __init__(self):
        self.energy = 100
        self.stability = 70
        self.trust = 50
        self.day_number = 1
        self.choices_history = {}
        self.processed_today = 0
        self.refused_today = 0
        self.allowed_today = 0

    def spend_energy(self, amount):
        self.energy = max(0, self.energy - amount)

    def change_stability(self, delta):
        self.stability = max(0, min(100, self.stability + delta))

    def change_trust(self, delta):
        self.trust = max(0, min(100, self.trust + delta))

    def apply_effects(self, effects: dict):
        if not effects:
            return
        if "energy" in effects:
            if effects["energy"] < 0:
                self.spend_energy(abs(effects["energy"]))
            else:
                self.energy += effects["energy"]
        if "stability" in effects:
            self.change_stability(effects["stability"])
        if "trust" in effects:
            self.change_trust(effects["trust"])

    def check_game_over(self):
        if self.energy <= 0 and self.stability < 10:
            return True
        return False

    def next_day(self):
        self.day_number += 1
        self.processed_today = 0
        self.refused_today = 0
        self.allowed_today = 0
