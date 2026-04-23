import pygame

class ProgressBar:

    def __init__(self, rect, color):
        self.rect = pygame.Rect(rect)
        self.color = color

    def draw(self, screen, value):
        pygame.draw.rect(screen, (50,50,50), self.rect)
        inner = self.rect.copy()
        inner.width = int(self.rect.width * (value / 100))
        pygame.draw.rect(screen, self.color, inner)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)
