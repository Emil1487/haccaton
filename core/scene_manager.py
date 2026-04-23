# core/scene_manager.py

class Scene:
    """Базовый класс сцены"""

    def __init__(self, game):
        self.game = game

    def on_enter(self, previous_scene):
        """Вызывается при входе в сцену"""
        pass

    def on_exit(self):
        """Вызывается при выходе из сцены"""
        pass

    def handle_event(self, event):
        """Обработка событий pygame"""
        pass

    def update(self, dt):
        """Логика сцены"""
        pass

    def render(self, surface):
        """Отрисовка сцены"""
        pass


class SceneManager:
    def __init__(self):
        self.current_scene = None

    def change_scene(self, new_scene):
        previous = self.current_scene

        if self.current_scene:
            self.current_scene.on_exit()

        self.current_scene = new_scene

        if self.current_scene:
            self.current_scene.on_enter(previous)

    def handle_event(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)

    def render(self, surface):
        if self.current_scene:
            self.current_scene.render(surface)
