# ui/typewriter.py

import pygame

class Typewriter:
    def __init__(self, text, font, speed=30, sound=None):
        self.full_text = text
        self.font = font
        self.speed = speed
        self.sound = sound

        self.current_text = ""
        self.timer = 0
        self.index = 0
        self.finished = False

    def update(self, dt):
        if self.finished:
            return

        self.timer += dt
        chars_to_add = int(self.timer * self.speed)

        if chars_to_add > 0:
            self.timer = 0

            for _ in range(chars_to_add):
                if self.index < len(self.full_text):
                    self.current_text += self.full_text[self.index]
                    self.index += 1

                    if self.sound:
                        self.sound.play()

                else:
                    self.finished = True
                    break

    def render(self, surface, pos, color):
        text_surf = self.font.render(self.current_text, True, color)
        surface.blit(text_surf, pos)

    def skip(self):
        self.current_text = self.full_text
        self.index = len(self.full_text)
        self.finished = True

    def is_complete(self):
        return self.finished
