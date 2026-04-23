# ui/resource_bar.py

import pygame
from config import *

class ResourceBar:
    def __init__(self, name, max_value, pos, size):
        self.name = name
        self.max_value = max_value
        self.value = max_value
        self.target_value = max_value

        self.pos = pos
        self.size = size

        self.font = pygame.font.SysFont("arial", 18)

    def set_value(self, value):
        self.target_value = max(0, min(self.max_value, value))

    def update(self, dt):
        diff = self.target_value - self.value
        self.value += diff * dt * 5

    def _get_color(self):
        ratio = self.value / self.max_value
        if ratio > 0.6:
            return (76, 175, 80)  # зелёный
        elif ratio > 0.3:
            return COLOR_ACCENT  # жёлтый
        else:
            return COLOR_DANGER  # красный

    def render(self, surface):
        x, y = self.pos
        w, h = self.size

        pygame.draw.rect(surface, COLOR_PANEL, (x, y, w, h))

        fill_width = int(w * (self.value / self.max_value))
        pygame.draw.rect(surface, self._get_color(), (x, y, fill_width, h))

        pygame.draw.rect(surface, COLOR_HIGHLIGHT, (x, y, w, h), 1)

        name_surf = self.font.render(self.name, True, COLOR_TEXT)
        value_surf = self.font.render(f"{int(self.value)}/{self.max_value}", True, COLOR_TEXT)

        surface.blit(name_surf, (x - 120, y))
        surface.blit(value_surf, (x + w + 10, y))
