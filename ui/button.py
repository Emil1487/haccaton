# ui/button.py

import pygame
from config import *

class Button:
    NORMAL = (27, 40, 56)      # #1B2838
    HOVER = (42, 63, 85)       # #2A3F55
    PRESSED = (13, 27, 42)     # #0D1B2A
    DISABLED = (51, 51, 51)    # #333333
    BORDER = (244, 211, 94)    # #F4D35E

    def __init__(self, rect, text, enabled=True):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.enabled = enabled

        self.font = pygame.font.SysFont("arial", 20)

        self.current_color = Button.NORMAL
        self.target_color = Button.NORMAL

        self.hovered = False
        self.pressed = False

        self.transition_speed = 10  # скорость смены цвета

    def is_clicked(self, event):
        if not self.enabled:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed and self.rect.collidepoint(event.pos):
                self.pressed = False
                return True
            self.pressed = False

        return False

    def update(self, dt):
        if not self.enabled:
            self.target_color = Button.DISABLED
        else:
            mouse_pos = pygame.mouse.get_pos()
            self.hovered = self.rect.collidepoint(mouse_pos)

            if self.pressed:
                self.target_color = Button.PRESSED
            elif self.hovered:
                self.target_color = Button.HOVER
            else:
                self.target_color = Button.NORMAL

        # Плавная интерполяция цвета
        self.current_color = tuple(
            int(self.current_color[i] + (self.target_color[i] - self.current_color[i]) * dt * self.transition_speed)
            for i in range(3)
        )

    def render(self, surface):
        pygame.draw.rect(surface, self.current_color, self.rect)

        # Рамка при hover
        if self.hovered and self.enabled:
            pygame.draw.rect(surface, Button.BORDER, self.rect, 2)

        text_surf = self.font.render(self.text, True, COLOR_TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
