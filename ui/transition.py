# ui/transition.py

import pygame

class Transition:
    def __init__(self, duration=0.8):
        self.duration = duration
        self.timer = 0
        self.active = False
        self.fade_in = True
        self.callback = None

    def start_fade_out(self, callback=None):
        self.active = True
        self.fade_in = False
        self.timer = 0
        self.callback = callback

    def start_fade_in(self):
        self.active = True
        self.fade_in = True
        self.timer = 0

    def update(self, dt):
        if not self.active:
            return

        self.timer += dt

        if self.timer >= self.duration:
            self.timer = self.duration
            if not self.fade_in and self.callback:
                self.callback()
            self.active = False

    def render(self, surface):
        if not self.active:
            return

        progress = self.timer / self.duration

        if self.fade_in:
            alpha = int(255 * (1 - progress))
        else:
            alpha = int(255 * progress)

        overlay = pygame.Surface(surface.get_size())
        overlay.fill((0, 0, 0))
        overlay.set_alpha(alpha)

        surface.blit(overlay, (0, 0))
