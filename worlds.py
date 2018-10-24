from rules import *

WORLDS_LIST = ['TestWorld', 'BetterWorld']


class World(object):

    def __init__(self, world_settings):
        self.world_settings = world_settings
        print(world_settings)

    @staticmethod
    def get_world(name, world_settings):
        return globals()[name](world_settings=world_settings)


class TestWorld(World):

    def __init__(self, world_settings):
        super().__init__(world_settings)
        print('TestWorld')


class BetterWorld(World):

    def __init__(self, world_settings):
        super().__init__(world_settings)
        print('TestWorld')
