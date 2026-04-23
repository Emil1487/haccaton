import pygame
from config import FONT_MEDIUM, WHITE, DARK_GRAY

class Button:

    def __init__(self, rect, text, callback):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.hover = False

    def draw(self, screen):
        color = (70,70,70) if not self.hover else (120,120,120)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)

        text_surf = FONT_MEDIUM.render(self.text, True, WHITE)
        screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
