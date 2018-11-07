from tools import *
import random


class World(object):

    def __init__(self, world_config):
        self.age = 0
        self.__set_attributes(world_config)
        self.__create_map()
        self.__pixel_randomizer()

    def __set_attributes(self, dict_config):
        attributes_dict = {}
        for _, v in dict_config.items():
            attributes_dict.update(v)
        self.__dict__.update(attributes_dict)

    def __create_map(self):
        self.map = [[0 for _ in range(self.world_size[0])] for _ in range(self.world_size[1])]

    def __occupy_world(self, occupy_method):
        self.__pixel_randomizer()

    def __pixel_randomizer(self):
        print('--------------------')
        pp.pprint(self.map)
        for _ in range(self.world_population):
            h = random.randrange(self.world_size[0]-1)
            v = random.randrange(self.world_size[1]-1)
            print(h, v)
            self.map[h][v] = 1
        print('--------------------')
        pp.pprint(self.map)

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
