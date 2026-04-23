# ui/text_box.py

import pygame
from config import *

class TextBox:
    def __init__(self, text, pos, max_width):
        self.text = text
        self.pos = pos
        self.max_width = max_width
        self.padding = 20

        self.font = pygame.font.SysFont("arial", 22)
        self.lines = self._wrap_text(text)

        self.background = pygame.Surface((1, 1), pygame.SRCALPHA)

        self._recalculate_size()

    def _wrap_text(self, text):
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            width, _ = self.font.size(test_line)

            if width <= self.max_width - self.padding * 2:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "

        lines.append(current_line)
        return lines

    def _recalculate_size(self):
        line_height = self.font.get_height()
        height = line_height * len(self.lines) + self.padding * 2

        self.background = pygame.Surface((self.max_width, height), pygame.SRCALPHA)
        self.background.fill((27, 40, 56, 230))  # прозрачный фон

        self.rect = self.background.get_rect(topleft=self.pos)

    def update(self, dt):
        pass

    def render(self, surface):
        surface.blit(self.background, self.rect)

        pygame.draw.rect(surface, COLOR_HIGHLIGHT, self.rect, 1)

        y_offset = self.rect.y + self.padding
        for line in self.lines:
            text_surf = self.font.render(line.strip(), True, COLOR_TEXT)
            surface.blit(text_surf, (self.rect.x + self.padding, y_offset))
            y_offset += self.font.get_height()
