# main.py

import pygame
import sys

from config import *
from core.game import Game


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()

    game = Game(screen, clock)
    game.run()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
