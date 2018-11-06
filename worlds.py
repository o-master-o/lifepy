from tools import *
# import numpy as np
import array
import pprint as pp


class World(object):

    def __init__(self, world_config):
        self.age = 0
        self.__set_world_attributes_(world_config)
        self.__create_map()

    def __set_world_attributes_(self, dict_config):
        self.__dict__.update(self.__get_typed_attributes(dict_config))
        print(self.__dict__)

    def __get_typed_attributes(self, dict_config):
        raw_config = self.__get_raw_attributes(dict_config)
        return {k: self.__auto_type(v) for k, v in raw_config.items()}

    def __get_raw_attributes(self, dict_config):
        raw_config = {}
        for _, v in dict_config.items():
            raw_config.update(v)
        print(raw_config)
        return raw_config

    def __auto_type(self, untyped_str):
        for fn in (self.__boolify, self.__listify, int, float):
            try:
                typed_str = fn(untyped_str)
                return typed_str
            except ValueError:
                pass
        return untyped_str

    def __boolify(self, untyped):
        if untyped == 'True':
            return True
        if untyped == 'False':
            return False
        raise ValueError("It is not bool Type")

    def __listify(self, untyped):
        if untyped[0] == '[' and untyped[-1] == ']':
            listified = untyped[1: -1].split(',')
            for i, item in enumerate(listified):
                listified[i] = self.__auto_type(item)
            return listified
        raise ValueError("It is not list")

    def __create_map(self):
        self.map = [[0 for _ in range(self.world_size[0])] for _ in range(self.world_size[1])]
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

    # def pixel_randomizer(self):
