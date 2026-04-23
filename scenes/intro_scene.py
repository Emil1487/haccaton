# scenes/intro_scene.py

import pygame
from core.scene_manager import Scene
from config import *
from scenes.morning_scene import MorningScene


class IntroScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.cards = [
            "Существуют места, где пересекаются пути миров.",
            "Последнее такое место — станция «Перекрёсток».",
            "Десять лет назад твоя сестра Лина ушла сюда работать.",
            "Она не вернулась.",
            "Теперь твоя очередь."
        ]

        self.font = pygame.font.SysFont("arial", 32)
        self.index = 0
        self.timer = 0
        self.phase = "fade_in"

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.next_card()

    def next_card(self):
        self.index += 1
        if self.index >= len(self.cards):
            self.game.transition.start_fade_out(
                lambda: self.game.scene_manager.change_scene(
                    MorningScene(self.game)
                )
            )
        else:
            self.timer = 0
            self.phase = "fade_in"

    def update(self, dt):
        self.timer += dt

        if self.phase == "fade_in" and self.timer >= 1:
            self.phase = "show"
            self.timer = 0
        elif self.phase == "show" and self.timer >= 3:
            self.phase = "fade_out"
            self.timer = 0
        elif self.phase == "fade_out" and self.timer >= 1:
            self.next_card()

    def render(self, surface):
        surface.fill((0, 0, 0))

        alpha = 255
        if self.phase == "fade_in":
            alpha = int(255 * (self.timer / 1))
        elif self.phase == "fade_out":
            alpha = int(255 * (1 - self.timer / 1))

        text = self.font.render(self.cards[self.index], True, (255, 255, 255))
        text.set_alpha(alpha)
        surface.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
