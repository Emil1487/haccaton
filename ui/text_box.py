import pygame
from config import FONT_MEDIUM, TYPEWRITER_EVENT

class TextBox:

    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.full_text = ""
        self.current_text = ""
        self.index = 0

    def set_text(self, text):
        self.full_text = text
        self.current_text = ""
        self.index = 0
        pygame.time.set_timer(TYPEWRITER_EVENT, 20)

    def update(self, event):
        if event.type == TYPEWRITER_EVENT:
            if self.index < len(self.full_text):
                self.current_text += self.full_text[self.index]
                self.index += 1
            else:
                pygame.time.set_timer(TYPEWRITER_EVENT, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, (20,20,20), self.rect)
        pygame.draw.rect(screen, (200,200,200), self.rect, 2)

        words = self.current_text.split(" ")
        lines = []
        line = ""
        for word in words:
            test = line + word + " "
            if FONT_MEDIUM.size(test)[0] < self.rect.width - 20:
                line = test
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)

        y = self.rect.y + 10
        for l in lines:
            surf = FONT_MEDIUM.render(l, True, (230,230,230))
            screen.blit(surf, (self.rect.x + 10, y))
            y += 30
