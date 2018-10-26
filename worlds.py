from rules import *
from tools import *


class World(object):

    def __init__(self, world_settings):
        self.world_settings = world_settings
        self.age = 0
        self.life_speed = 1/float(self.world_settings['world_life_speed'])
        self.world_map = self.world_settings['world_size'].split(',')
        self.life_time = int(self.world_settings['world_life_time'])
        self.population = int(self.world_settings['world_population'])
        # self.pixel_settings = int(self.world_settings['pixel_settings'])
        self.pixels = []
        for count in range(self.population):
            x = Pixel(name=count)
            x.attr = count
            self.pixels.append(x)

        print(world_settings)

    def get_age(self):
        return self.age

    def get_life_speed(self):
        log('life_speed: ', self.life_speed)
        return self.life_speed

    def get_world_life_time(self):
        log('world_life_time: ', self.life_time)
        return self.life_time

    def update_world(self):
        log('world_age: ', self.age)
        self.age = self.age + 1
        self.__update_pixels()

    def __update_pixels(self):
        for pixel in self.pixels:
            print('update pixel: ', pixel.name)


class Pixel(object):

    def __init__(self, name):
        self.name = name
        self.sex = 'm'
        self.age = 0
        # self.life_time = pixel_settings['life_time']
    #     self.reproduction_period = pixel_settings['reproduction_period']
    #
    # def coitus(self):
    #     pass
    #
    # def walk(self):
    #     pass
    #
    # def __del__(self):
    #     print(self.name, 'died')
    #
    # def die(self):
    #     self.__init__()
