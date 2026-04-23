# entities/dialogue.py

import json
from config import DATA_PATH


class DialogueManager:
    def __init__(self):
        with open(DATA_PATH + "dialogues.json", "r", encoding="utf-8") as f:
            self.dialogues = json.load(f)

    def load_dialogue(self, dialogue_id) -> dict:
        return self.dialogues.get(dialogue_id)

    def get_node(self, dialogue_id, node_id) -> dict:
        return self.dialogues[dialogue_id]["nodes"].get(node_id)

    def get_choices(self, node, event_system):
        choices = node.get("choices", [])
        filtered = []

        for choice in choices:
            conditions = choice.get("conditions")
            if event_system.check_condition(conditions):
                filtered.append(choice)

        return filtered

    def apply_consequences(self, consequences, resources, event_system):
        if not consequences:
            return

        resources.modify_stability(consequences.get("stability", 0))
        resources.modify_trust(consequences.get("trust", 0))
        resources.modify_attention(consequences.get("attention", 0))

        energy = consequences.get("energy", 0)
        if energy < 0:
            resources.spend_energy(-energy)
        else:
            resources.energy = min(resources.max_energy, resources.energy + energy)

        flags = consequences.get("flags", {})
        for key, value in flags.items():
            event_system.set_flag(key, value)
