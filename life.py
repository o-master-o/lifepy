import time
from ui.view import View
from model.world import WorldOne


class LifeController:
    def __init__(self, view, world):
        self.view = view
        self.world = world
        self.age = 0
        self.max_age = self.view.get_max_age()
        self.sleep_time = self._set_sleep_time(self.view.get_speed())

    @staticmethod
    def _set_sleep_time(speed):
        return 1.0 / speed

    def run_life(self):
        self.world.grid = self.view.get_grid()
        while self.age <= self.max_age:
            self.view.draw_step(self.world.grid(self.world.make_life_step()))

            self.age += 1
            time.sleep(self.sleep_time)


if __name__ == '__main__':
    app = LifeController(View(), WorldOne(60, 100))
