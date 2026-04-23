import pygame
import random
from config import *
from engine.game_state import GameState
from core.resource_manager import GameManager
from core.day_manager import DayManager
from scenes.main_menu import MainMenu
from scenes.hub_scene import HubScene
from scenes.dialogue_scene import DialogueScene
from scenes.report_scene import ReportScene

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("СМОТРИТЕЛЬ ПЕРЕКРЁСТКА")

clock = pygame.time.Clock()

game_manager = GameManager()
day_manager = DayManager()

current_state = GameState.MENU
scene = MainMenu(screen)

running = True
glitch_timer = 0

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        scene.handle_event(event)

    scene.update()

    # Эффекты
    screen.fill(DARK_GRAY)

    # Пыль (particles)
    for _ in range(3):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        pygame.draw.circle(screen, (200,200,200), (x,y), 1)

    scene.draw()

    # Мерцание при низкой стабильности
    if game_manager.stability < 20:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(random.randint(20,60))
        overlay.fill((200,0,0))
        screen.blit(overlay, (0,0))

    pygame.display.flip()

pygame.quit()
