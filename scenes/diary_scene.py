class DiaryScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("arial", 24, italic=True)
        self.typewriter = Typewriter(
            "Запись Лины: Сегодня я впервые услышала, как портал поёт...",
            self.font, speed=20
        )
        self.button = Button((500, 600, 300, 50), "Закрыть")

    def handle_event(self, event):
        if self.button.is_clicked(event):
            from scenes.morning_scene import MorningScene
            self.game.scene_manager.change_scene(MorningScene(self.game))

    def update(self, dt):
        self.typewriter.update(dt)
        self.button.update(dt)

    def render(self, surface):
        surface.fill((245, 230, 202))
        self.typewriter.render(surface, (100, 200), (50, 50, 50))
        self.button.render(surface)
