from render import *
from worlds import *
from tools import *
import time
# import pygame


DEFAULTS_CONFIG_FILE_PATH = r'{}'.format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'defaults.ini'))
CONFIG_FILE_PATH = r'{}'.format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.ini'))


def start_game():
    config_inst = AdvancedConfigParser()
    config_inst.read([DEFAULTS_CONFIG_FILE_PATH, CONFIG_FILE_PATH])
    world_config = config_inst.filter_dict(['world-config', 'pixel-config'])

    world_instance = World(world_config)
    pp.pprint(world_instance.__dict__)

    world_life_time = world_instance.get_world_life_time()
    world_life_speed = world_instance.get_life_speed()
    while world_life_time >= world_instance.get_age():
        world_instance.update_world()
        time.sleep(world_life_speed)


if __name__ == '__main__':
    start_game()
