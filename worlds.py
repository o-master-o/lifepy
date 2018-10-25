from rules import *
from tools import *


class World(object):

    def __init__(self, world_settings):
        self.world_settings = world_settings
        self.age = 0
        self.world_life_time = int(self.world_settings['world_life_time'])
        print(world_settings)

    def get_age(self):
        log(self.age)
        return self.age

    def get_world_life_time(self):
        log(self.age)
        return self.world_life_time

    def update(self):
        self.age = self.age + 1
