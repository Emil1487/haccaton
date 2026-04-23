class EndingScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("arial", 32)
        ending_id = game.event_system.calculate_ending()

        self.text = {
            "ending_merciful": "Ты спас многих. Но цена была велика.",
            "ending_harsh": "Портал стабилен. Люди — нет.",
            "ending_balanced": "Ты сохранил равновесие."
        }[ending_id]

        self.button = Button((500, 600, 300, 50), "Главное меню")

    def handle_event(self, event):
        if self.button.is_clicked(event):
            from scenes.menu_scene import MenuScene
            self.game.scene_manager.change_scene(MenuScene(self.game))

    def update(self, dt):
        self.button.update(dt)

    def render(self, surface):
        surface.fill((0, 0, 0))
        txt = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(txt, txt.get_rect(center=(SCREEN_WIDTH//2, 300)))
        self.button.render(surface)
