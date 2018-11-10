from tools import *
import random
import os


class World(object):

    def __init__(self, world_config):
        self.__set_attributes(world_config)
        self.__age = 0
        self.__create_map()
        self.__occupy_world()

    def __set_attributes(self, dict_config):
        for _, config_section in dict_config.items():
            for attribute, value in config_section.items():
                setattr(self, attribute, value)

    def __create_map(self):
        self.map = [[0 for _ in range(self.world_size[0])]
                    for _ in range(self.world_size[1])]

    def __occupy_world(self, **kwargs):
        self.__pixel_randomizer()

    def __pixel_randomizer(self):
        rand_points = self.__generate_uniq_pixels(self.world_size[0], self.world_size[1], self.world_population)
        for i in rand_points:
            self.__invade_pixel_on_map(i)

    def __generate_uniq_pixels(self, w, h, n):
        return [divmod(i, w) for i in random.sample(range(w * h), n)]

    def __invade_pixel_on_map(self, pixel):
        self.map[pixel[0]][pixel[1]] = 1

    def get_age(self):
        return self.__age

    def get_life_speed(self):
        log('life_speed: ', self.life_speed)
        return 1/float(self.life_speed)

    def get_world_life_time(self):
        log('world_life_time: ', self.life_time)
        return self.life_time

    def update_world(self):
        self.__update_map()
        os.system('clear')
        log('world_age: ', self.__age)
        self.__age = self.__age + 1

    def __update_map(self):
        temp_map = [[self.__spawn_pixel() for _ in range(self.world_size[0])] for _ in range(self.world_size[1])]

    def __spawn_pixel(self):
        pass

    def __check_pixel_age(self):
        pass
