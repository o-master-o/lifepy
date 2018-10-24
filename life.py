from render import *
from worlds import *
import time
import timeit
import pygame
import configparser

CONFIG_FILE_PATH = r'settings.txt'


def start_game():
    config_inst = configparser.RawConfigParser()
    config_inst.read(CONFIG_FILE_PATH)
    selected_world = config_inst.get(section='game-config', option='world')
    world_settings = dict(config_inst.items(section='world-config'))

    world_instance = World.get_world(selected_world, world_settings)
    print(type(world_settings['world_life_time']))
    #
    # while world_life_time:
    #     world_instance.


if __name__ == '__main__':
    start_game()



# t = Timer(30.0, hello)
# t.start() # after 30 seconds, "hello, world" will be printed
