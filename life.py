from worlds import *
import time
from render import *

# import pygame


DEFAULTS_CONFIG_FILE_PATH = r'{}'.format(os.path.join(os.path.dirname(
    os.path.abspath(__file__)),
    'defaults.json'))
CONFIG_FILE_PATH = r'{}'.format(os.path.join(os.path.dirname(
    os.path.abspath(__file__)),
    'settings.json'))


def start_game():
    config_inst = JSONConfigParser()
    config_inst.read(DEFAULTS_CONFIG_FILE_PATH, CONFIG_FILE_PATH)
    game_config = config_inst.filter_dict(['game_config'])['game_config']
    pp.pprint(game_config)
    pp.pprint(game_config['rendering_method'])
    world_config = config_inst.filter_dict(['world_config'])

    world_instance = World(world_config)
    pp.pprint(world_instance.__dict__)
    renderer_instance = Renderer(game_config['rendering_method'])

    world_life_time = world_instance.get_world_life_time()
    world_life_speed = world_instance.get_life_speed()
    while world_life_time >= world_instance.get_age():
        world_instance.update_world()
        renderer_instance.draw_world(world_instance.map)
        time.sleep(world_life_speed)


if __name__ == '__main__':
    start_game()
