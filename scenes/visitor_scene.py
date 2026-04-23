# scenes/visitor_scene.py

import pygame
import json
from core.scene_manager import Scene
from config import *
from ui.button import Button
from ui.text_box import TextBox
from ui.portrait import Portrait
from ui.typewriter import Typewriter
from entities.visitor import Visitor
from entities.dialogue import DialogueManager
from scenes.evening_scene import EveningScene


class VisitorScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.dialogue_manager = DialogueManager()

        with open(DATA_PATH + "visitors.json", encoding="utf-8") as f:
            visitors = json.load(f)

        self.visitor = Visitor(visitors[game.current_day - 1])

        self.dialogue = self.dialogue_manager.load_dialogue(
            self.visitor.dialogue_id
        )

        self.node_id = self.dialogue["start"]
        self.node = self.dialogue["nodes"][self.node_id]

        self.font = pygame.font.SysFont("arial", 24)

        self.typewriter = Typewriter(self.node["text"], self.font)
        self.buttons = []
        self._create_choice_buttons()

        self.portrait = Portrait(
            self.visitor.portrait_path,
            self.visitor.get_origin_color(),
            (50, 150)
        )

    def _create_choice_buttons(self):
        self.buttons.clear()
        if not self.typewriter.is_complete():
            return

        choices = self.dialogue_manager.get_choices(
            self.node,
            self.game.event_system
        )

        for i, choice in enumerate(choices):
            btn = Button((400, 450 + i * 60, 600, 50),
                         choice["text"])
            btn.choice_data = choice
            self.buttons.append(btn)

    def handle_event(self, event):
        if not self.typewriter.is_complete():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.typewriter.skip()
            return

        for btn in self.buttons:
            if btn.is_clicked(event):
                self._apply_choice(btn.choice_data)

    def _apply_choice(self, choice):
        self.dialogue_manager.apply_consequences(
            choice.get("consequences"),
            self.game.resources,
            self.game.event_system
        )

        if choice["next"] == "end":
            self.game.transition.start_fade_out(
                lambda: self.game.scene_manager.change_scene(
                    EveningScene(self.game)
                )
            )
        else:
            self.node_id = choice["next"]
            self.node = self.dialogue["nodes"][self.node_id]
            self.typewriter = Typewriter(self.node["text"], self.font)

    def update(self, dt):
        self.typewriter.update(dt)
        self.portrait.update(dt)

        if self.typewriter.is_complete():
            self._create_choice_buttons()

        for btn in self.buttons:
            btn.update(dt)

    def render(self, surface):
        surface.fill(COLOR_BACKGROUND)

        self.portrait.render(surface)

        name_text = self.font.render(
            f"{self.visitor.name} | {self.visitor.origin} → {self.visitor.destination}",
            True, COLOR_TEXT
        )
        surface.blit(name_text, (300, 150))

        self.typewriter.render(surface, (300, 250), COLOR_TEXT)

        for btn in self.buttons:
            btn.render(surface)
