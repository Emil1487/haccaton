class EveningScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("arial", 32)
        self.button = Button((500, 600, 300, 50), "Продолжить")

    def handle_event(self, event):
        if self.button.is_clicked(event):
            self.game.current_day += 1
            if self.game.current_day > 2:
                from scenes.ending_scene import EndingScene
                self.game.scene_manager.change_scene(EndingScene(self.game))
            else:
                from scenes.morning_scene import MorningScene
                self.game.scene_manager.change_scene(MorningScene(self.game))

    def update(self, dt):
        self.button.update(dt)

    def render(self, surface):
        surface.fill(COLOR_BACKGROUND)
        text = self.font.render(f"Конец дня {self.game.current_day}", True, COLOR_ACCENT)
        surface.blit(text, (400, 200))
        self.button.render(surface)
