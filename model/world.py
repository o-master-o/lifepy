from itertools import count
from abc import ABCMeta, abstractmethod
import numpy as np


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

        self._grid = self._build_grid(column_number, row_number)
        self.age_counter = count()
        self._age = 0

    @staticmethod
    def _build_grid(column_number, row_number):
        return np.zeros((column_number, row_number), dtype=bool)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, value):
        self._grid = value

    def apply_init_map(self, init_map):
        self._grid = init_map

    def get_grid(self):
        return self._grid

    def make_life_step(self):
        self._age = next(self.age_counter)
        nbrs_count = sum(np.roll(np.roll(self._grid, i, 0), j, 1)
                         for i in (-1, 0, 1) for j in (-1, 0, 1)
                         if (i != 0 or j != 0))
        return (nbrs_count == 3) | (self._grid & (nbrs_count == 2))

