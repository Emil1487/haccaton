# core/event_system.py

class EventSystem:
    def __init__(self):
        self.flags = {}
        self.decisions = []  # (day, visitor_id, choice_id)

    def set_flag(self, key, value=True):
        self.flags[key] = value

    def get_flag(self, key, default=False) -> bool:
        return self.flags.get(key, default)

    def add_decision(self, day, visitor_id, choice_id):
        self.decisions.append({
            "day": day,
            "visitor": visitor_id,
            "choice": choice_id
        })

    def check_condition(self, conditions_dict) -> bool:
        if not conditions_dict:
            return True

        for key, expected in conditions_dict.items():
            if self.flags.get(key) != expected:
                return False
        return True

    def get_mercy_score(self) -> int:
        return sum(1 for d in self.decisions if "pass" in d["choice"])

    def get_cruel_score(self) -> int:
        return sum(1 for d in self.decisions if "reject" in d["choice"])

    def calculate_ending(self) -> str:
        mercy = self.get_mercy_score()
        cruel = self.get_cruel_score()

        if mercy >= cruel + 2:
            return "ending_merciful"
        elif cruel >= mercy + 2:
            return "ending_harsh"
        else:
            return "ending_balanced"
