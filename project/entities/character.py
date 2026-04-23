import json
import os
import pygame
from config import DATA_DIR

class Character:

    def __init__(self, char_id):
        with open(os.path.join(DATA_DIR, "characters.json"), encoding="utf-8") as f:
            data = json.load(f)

        self.data = next(c for c in data if c["id"] == char_id)
        self.id = self.data["id"]
        self.name = self.data["name"]
        self.dialogue = self.data["dialogue"]
        self.portrait_path = self.data.get("portrait", None)

    def get_node(self, node):
        return self.dialogue.get(node, None)

    def load_portrait(self):
        if self.portrait_path and os.path.exists(self.portrait_path):
            return pygame.image.load(self.portrait_path)
        return None
