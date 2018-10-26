from render import *
from worlds import *
import time
from tools import *
import os
import pprint as pp
# import timeit
# import pygame
import configparser
DEFAULTS_CONFIG_FILE_PATH = r'{}'.format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'defaults.ini'))
CONFIG_FILE_PATH = r'{}'.format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.ini'))


def start_game():
    config_inst = AdvancedConfigParser()
    config_inst.read([DEFAULTS_CONFIG_FILE_PATH, CONFIG_FILE_PATH])
    # world_settings = dict(config_inst.items(section='world-config'))
    print(config_inst.sections())
    f_dict = config_inst.get_filtered_dict(['world-config', 'pixel-config'])
    # config_dict = config_inst.get_dict()
    # world_config = config_dict.update({config_dict['world-config']})
    pp.pprint(config_inst.dict_config)
    print('-----------------------------')
    pp.pprint(f_dict)

    # world_instance = World({'world-config': config_dict['world-config'], })

    # world_life_time = world_instance.get_world_life_time()
    # world_life_speed = world_instance.get_life_speed()
    # while world_life_time > world_instance.get_age():
    #     world_instance.update_world()
    #     time.sleep(world_life_speed)


if __name__ == '__main__':
    start_game()
