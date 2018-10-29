from tools import *
import numpy as np
import pprint as pp


class World(object):

    def __init__(self, world_config):
        self.world_config = world_config
        self.age = 0
        self.life_speed = 1/float(self.world_config['world-config']['world_life_speed'])
        self.world_size = self.world_config['world-config']['world_size'].split(',')
        self.life_time = int(self.world_config['world-config']['world_life_time'])
        self.population = int(self.world_config['world-config']['world_population'])
        print(type(self.world_size))
        # self.map = self.__map_creator()
        self.__map_creator()


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
        # self.__update_pixels()
    #
    # def __update_pixels(self):
    #     for pixel in self.pixels:
    #         print('update pixel: ', pixel.name)

    # def pixel_randomizer(self):
    def __map_creator(self):
        # return np.array([[0 for _ in range(int(self.world_size[1]))] for _ in range(int(self.world_size[2]))])
        return np.array([[0 for _ in range(int(self.world_size[1]))] for _ in range(int(self.world_size[2]))])
        # my_list = [0 for _ in range(int(self.world_size[1]))]
        # my_list = [my_list for _ in range(int(self.world_size[2]))]
        # print(my_list)



#
# class Pixel(object):
#
#     def __init__(self, name):
#         self.name = name
#         self.sex = 'm'
#         self.age = 0
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
