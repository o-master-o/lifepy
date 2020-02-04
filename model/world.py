from itertools import count
from abc import ABCMeta, abstractmethod


class World(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, row_number: int, column_number: int):
        pass

    @abstractmethod
    def make_life_step(self):
        raise NotImplementedError("Please Implement this method")


class WorldOne(World):

    def __init__(self, row_number, column_number):
        super().__init__(row_number, column_number)

        self.grid = self._build_grid(column_number, row_number)
        self.age_counter = count()
        self.age = 0

    @staticmethod
    def _build_grid(column_number, row_number):
        return [[0 for _ in range(column_number)]
                for _ in range(row_number)]

    def apply_init_map(self, init_map):
        self.grid = init_map

    def get_grid(self):
        return self.grid

    def make_life_step(self):
        self.age = next(self.age_counter)

        return self.age
