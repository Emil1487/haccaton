import os
import pygame

# Экран
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Цвета
WHITE = (240, 240, 240)
BLACK = (15, 15, 15)
DARK_GRAY = (30, 30, 30)
RED = (200, 60, 60)
BLUE = (70, 120, 220)
GOLD = (200, 170, 60)
GREEN = (80, 200, 120)

# Пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Шрифты
pygame.font.init()
FONT_NAME = pygame.font.match_font("arial")  # поддерживает кириллицу
FONT_SMALL = pygame.font.Font(FONT_NAME, 20)
FONT_MEDIUM = pygame.font.Font(FONT_NAME, 28)
FONT_LARGE = pygame.font.Font(FONT_NAME, 40)

TYPEWRITER_EVENT = pygame.USEREVENT + 1
