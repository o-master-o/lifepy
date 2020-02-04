import tkinter as tk
from ui import gui


class View(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.iconbitmap(r'resources/app_icon.ico')
        self.window = gui.create_main_window(self.root)
        self.root.protocol("WM_DELETE_WINDOW", gui.destroy_main_window)
        self.root.mainloop()

    def get_max_age(self):
        return self.window.max_age

    def get_age(self):
        return self.window.age

    def get_speed(self):
        return self.window.speed


