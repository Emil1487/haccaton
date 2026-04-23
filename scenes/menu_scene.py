# scenes/menu_scene.py

import pygame
import math
from core.scene_manager import Scene
from config import *
from ui.button import Button
from scenes.intro_scene import IntroScene


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.title_font = pygame.font.SysFont("arial", 48)
        self.subtitle_font = pygame.font.SysFont("arial", 18)

        center_x = SCREEN_WIDTH // 2
        start_y = 300

        self.buttons = [
            Button((center_x - 150, start_y + i * 65, 300, 50), text)
            for i, text in enumerate([
                "Новая игра",
                "Продолжить",
                "Настройки",
                "Выход"
            ])
        ]

        self.lights = []
        for i in range(5):
            self.lights.append({
                "x": 200 + i * 200,
                "y": 150 + i * 50,
                "radius": 5 + i,
                "phase": i
            })

        self.time = 0

    def handle_event(self, event):
        for i, btn in enumerate(self.buttons):
            if btn.is_clicked(event):
                if i == 0:
                    self.game.transition.start_fade_out(
                        lambda: self.game.scene_manager.change_scene(IntroScene(self.game))
                    )
                elif i == 3:
                    self.game.quit()

    def update(self, dt):
        self.time += dt
        for btn in self.buttons:
            btn.update(dt)

    def render(self, surface):
        surface.fill(COLOR_BACKGROUND)

        for light in self.lights:
            alpha = 128 + 127 * math.sin(self.time * 2 + light["phase"])
            glow = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(glow, (168, 218, 220, int(alpha)),
                               (10, 10), light["radius"])
            surface.blit(glow, (light["x"], light["y"]))

        title = self.title_font.render("Смотритель Перекрёстка", True, COLOR_ACCENT)
        subtitle = self.subtitle_font.render("Выбор без победителей", True, COLOR_HIGHLIGHT)

        surface.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 180)))
        surface.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH // 2, 230)))

        for btn in self.buttons:
            btn.render(surface)
