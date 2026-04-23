# entities/resources.py

class Resources:
    def __init__(self):
        self.max_energy = 25
        self.max_stability = 100
        self.max_trust = 100
        self.max_attention = 100

        self.energy = 20
        self.stability = 80
        self.trust = 50
        self.attention = 10

    # ---------- ЭНЕРГИЯ ----------
    def spend_energy(self, amount) -> bool:
        if self.energy >= amount:
            self.energy -= amount
            return True
        return False

    def restore_energy(self):
        if self.stability > 50:
            self.energy += 3
        elif 20 <= self.stability <= 50:
            self.energy += 1
        else:
            self.energy += 0

        self.energy = min(self.energy, self.max_energy)

    # ---------- МОДИФИКАТОРЫ ----------
    def modify_stability(self, delta):
        self.stability = max(0, min(self.max_stability, self.stability + delta))

    def modify_trust(self, delta):
        self.trust = max(0, min(self.max_trust, self.trust + delta))

    def modify_attention(self, delta):
        self.attention = max(0, min(self.max_attention, self.attention + delta))

    # ---------- СОСТОЯНИЯ ----------
    def is_critical(self) -> bool:
        return self.energy <= 3 or self.stability <= 20

    def is_game_over(self) -> bool:
        return self.energy == 0

    def get_all(self) -> dict:
        return {
            "energy": self.energy,
            "stability": self.stability,
            "trust": self.trust,
            "attention": self.attention
        }
