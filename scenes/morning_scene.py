# scenes/morning_scene.py

import pygame
from core.scene_manager import Scene
from config import *
from ui.button import Button
from ui.resource_bar import ResourceBar
from ui.typewriter import Typewriter
from scenes.visitor_scene import VisitorScene


class MorningScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.title_font = pygame.font.SysFont("arial", 40)
        self.small_font = pygame.font.SysFont("arial", 24)

        self.resources_ui = [
            ResourceBar("Энергия", 25, (900, 50), (200, 20)),
            ResourceBar("Стабильность", 100, (900, 80), (200, 20)),
            ResourceBar("Доверие", 100, (900, 110), (200, 20)),
            ResourceBar("Внимание", 100, (900, 140), (200, 20)),
        ]

        self.echo_text = Typewriter(
            f"Эхо: Сегодня {3} посетителя. Стабильность портала нестабильна.",
            self.small_font
        )

        self.start_button = Button((SCREEN_WIDTH//2 - 150, 600, 300, 50),
                                   "Начать приём")

    def handle_event(self, event):
        if self.start_button.is_clicked(event):
            self.game.transition.start_fade_out(
                lambda: self.game.scene_manager.change_scene(
                    VisitorScene(self.game)
                )
            )

    def update(self, dt):
        self.echo_text.update(dt)
        self.start_button.update(dt)

        res = self.game.resources
        values = res.get_all()

        for bar in self.resources_ui:
            if bar.name == "Энергия":
                bar.set_value(values["energy"])
            elif bar.name == "Стабильность":
                bar.set_value(values["stability"])
            elif bar.name == "Доверие":
                bar.set_value(values["trust"])
            elif bar.name == "Внимание":
                bar.set_value(values["attention"])

            bar.update(dt)

    def render(self, surface):
        surface.fill(COLOR_BACKGROUND)

        title = self.title_font.render(f"День {self.game.current_day}", True, COLOR_ACCENT)
        subtitle = self.small_font.render("Утро", True, COLOR_TEXT)

        surface.blit(title, (50, 50))
        surface.blit(subtitle, (50, 100))

        self.echo_text.render(surface, (50, 200), COLOR_TEXT)

        for bar in self.resources_ui:
            bar.render(surface)

        self.start_button.render(surface)
