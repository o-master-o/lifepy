from render import *
from worlds import *
import time
# import timeit
# import pygame
import configparser

DEFAULTS_CONFIG_FILE_PATH = r'defaults.ini'
CONFIG_FILE_PATH = r'settings.ini'


def start_game():
    config_inst = configparser.RawConfigParser()
    config_inst.read([DEFAULTS_CONFIG_FILE_PATH, CONFIG_FILE_PATH])
    world_settings = dict(config_inst.items(section='world-config'))
    world_instance = World(world_settings)

    world_life_time = world_instance.get_world_life_time()
    world_life_speed = world_instance.get_life_speed()
    while world_life_time > world_instance.get_age():
        world_instance.update_world()
        time.sleep(world_life_speed)


if __name__ == '__main__':
    start_game()
