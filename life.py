from render import *
from worlds import *
import time
# import timeit
# import pygame
import configparser

CONFIG_FILE_PATH = r'settings.txt'


def start_game():
    config_inst = configparser.RawConfigParser()
    config_inst.read(CONFIG_FILE_PATH)
    world_settings = dict(config_inst.items(section='world-config'))
    print(world_settings)
    world_instance = World(world_settings)

    world_life_time = world_instance.get_world_life_time()
    world_age = world_instance.get_age()
    while world_life_time > world_age:
        world_age = world_instance.get_age()
        world_instance.update()
        time.sleep(1)


if __name__ == '__main__':
    start_game()



# t = Timer(30.0, hello)
# t.start() # after 30 seconds, "hello, world" will be printed
