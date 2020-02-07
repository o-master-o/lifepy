from tkinter import Tk, Canvas
import numpy as np


class Cell(object):
    LIVE_COLOR_BG = "#9932CC"
    DEAD_COLOR_BG = "#bbbbbb"
    LIVE_COLOR_BORDER = "#9932CC"
    DEAD_COLOR_BORDER = "#cccccc"

    def __init__(self, master, x, y, size):
        self.master = master
        self.x = x
        self.y = y
        self.size = size
        self._live = False

    @property
    def live(self):
        return self._live

    @live.setter
    def live(self, value):
        self._live = value

    def switch(self):
        """ Switch cell status """
        self._live = not self._live

    def draw(self):
        """ draw Cell on the canvas """
        if self.master:
            fill = self.LIVE_COLOR_BG
            outline = self.LIVE_COLOR_BORDER

            if not self._live:
                fill = self.DEAD_COLOR_BG
                outline = self.DEAD_COLOR_BORDER

            x1 = self.x * self.size
            x2 = x1 + self.size
            y1 = self.y * self.size
            y2 = y1 + self.size

            self.master.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)


class CanvasGrid(Canvas):
    def __init__(self, master, row_number, column_number, cell_size):
        Canvas.__init__(self, master, width=cell_size * column_number,
                        height=cell_size * row_number)

        self.cellSize = cell_size

        self.grid = [[Cell(self, column, row, cell_size)
                      for column in range(column_number)]
                     for row in range(row_number)]

        self.switched = []  # avoid multi switching of state during mouse motion.

        self.bind("<Button-1>", self.handle_mouse_click)
        self.bind("<B1-Motion>", self.handle_mouse_motion)
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _event_coordinates(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handle_mouse_click(self, event):
        row, column = self._event_coordinates(event)
        cell = self.grid[row][column]
        cell.switch()
        cell.draw()
        self.switched.append(cell)

    def handle_mouse_motion(self, event):
        row, column = self._event_coordinates(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell.switch()
            cell.draw()
            self.switched.append(cell)

    def get_grid(self):
        return np.array([[y.live for y in x] for x in self.grid])
