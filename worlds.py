from rules import *
from tools import *


class World(object):

    def __init__(self, world_settings):
        self.world_settings = world_settings
        self.age = 0
        self.life_speed = 1/float(self.world_settings['world_life_speed'])
        self.world_size = []
        self.world_life_time = int(self.world_settings['world_life_time'])
        print(world_settings)

    def get_age(self):
        return self.age

    def get_life_speed(self):
        log('life_speed: ', self.life_speed)
        return self.life_speed

    def get_world_life_time(self):
        log('world_life_time: ', self.world_life_time)
        return self.world_life_time

    def update_world(self):
        log('world_age: ', self.age)
        self.age = self.age + 1
