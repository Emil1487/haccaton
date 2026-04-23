from enum import Enum

class GameState(Enum):
    MENU = 0
    HUB = 1
    DIALOGUE = 2
    REPORT = 3
    GAME_OVER = 4
