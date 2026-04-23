class MapScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("arial", 28)
        self.back_button = Button((50, 650, 200, 50), "Назад")

    def handle_event(self, event):
        if self.back_button.is_clicked(event):
            self.game.scene_manager.change_scene(
                MorningScene(self.game)
            )

    def update(self, dt):
        self.back_button.update(dt)

    def render(self, surface):
        surface.fill(COLOR_BACKGROUND)
        text = self.font.render("Карта маршрутов", True, COLOR_ACCENT)
        surface.blit(text, (500, 100))
        self.back_button.render(surface)
