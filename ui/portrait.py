# ui/portrait.py

import pygame

class Portrait:
    def __init__(self, image_path, world_color, pos):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 280))

        self.world_color = world_color
        self.pos = pos

        self.alpha = 0
        self.fade_duration = 0.5
        self.timer = 0

    def update(self, dt):
        if self.alpha < 255:
            self.timer += dt
            progress = min(1, self.timer / self.fade_duration)
            self.alpha = int(255 * progress)

    def render(self, surface):
        x, y = self.pos

        bg_rect = pygame.Rect(x, y, 200, 280)
        pygame.draw.rect(surface, self.world_color, bg_rect)

        image_copy = self.image.copy()
        image_copy.set_alpha(self.alpha)

        surface.blit(image_copy, (x, y))

        pygame.draw.rect(surface, (168, 218, 220), bg_rect, 2)
