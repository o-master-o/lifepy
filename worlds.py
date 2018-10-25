from rules import *
from tools import *


class World(object):

    def __init__(self, world_settings):
        self.world_settings = world_settings
        self.age = 0
        self.life_speed = 1/float(self.world_settings['world_life_speed'])
        self.world_map = self.world_settings['world_size'].split(',')
        self.world_life_time = int(self.world_settings['world_life_time'])
        self.world_population = int(self.world_settings['world_population'])
        self.pixel_life_time = int(self.world_settings['pixel_life_time'])
        self. simplelist = []
        for count in range(self.world_population):
            x = Pixel()
            x.attr = count
            simplelist.append(x)

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
        __update_pixels()

    def __update_pixels(self):
        for pixel in world_population:
            pass


class Pixel(object):

    def __init__(self, pixel_life_time):
        self.pixel_life_time = pixel_life_time
        self.age = 0
