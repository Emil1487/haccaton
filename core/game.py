# core/game.py

import pygame
from config import *
from core.scene_manager import SceneManager, Scene


class TestScene(Scene):
    """Временная сцена для проверки работы"""

    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("arial", 36)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.quit()

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(COLOR_BACKGROUND)

        text = self.font.render("Смотритель Перекрёстка", True, COLOR_ACCENT)
        hint = self.font.render("Нажмите ESC для выхода", True, COLOR_TEXT)

        surface.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, 300)))
        surface.blit(hint, hint.get_rect(center=(SCREEN_WIDTH // 2, 400)))


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.scene_manager = SceneManager()

        # Запускаем тестовую сцену
        self.scene_manager.change_scene(TestScene(self))

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # delta time в секундах

            self._handle_events()
            self._update(dt)
            self._render()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            else:
                self.scene_manager.handle_event(event)

    def _update(self, dt):
        self.scene_manager.update(dt)

    def _render(self):
        self.scene_manager.render(self.screen)
        pygame.display.flip()

    def quit(self):
        self.running = False
