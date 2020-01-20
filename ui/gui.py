#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 07, 2020 01:16:17 AM CET  platform: Linux

import sys
from ui import grid_field
# from model import world

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

rt = None


def create_main_window(root, *args, **kwargs):
    global rt
    rt = root
    top_window = MainWindow(root)
    return top_window


def destroy_main_window():
    global rt
    rt.destroy()
    rt = None


class MainWindow(object):
    def __init__(self, top=None):
        self.top = top
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bg_color = '#d9d9d9'  # X11 color: 'gray85'
        _fg_color = '#000000'  # X11 color: 'black'
        _comp_color = '#d9d9d9'  # X11 color: 'gray85'
        _ana_1_color = '#d9d9d9'  # X11 color: 'gray85'
        _ana_2_color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bg_color)
        self.style.configure('.', foreground=_fg_color)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _comp_color),
                                        ('active', _ana_2_color)])

        self.top.geometry("1215x620+181+78")
        self.top.minsize(1, 1)
        self.top.maxsize(1585, 870)
        self.top.resizable(1, 1)
        self.top.title("LifePy")
        self.top.configure(relief="ridge")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.009, rely=0.014, relheight=0.237, relwidth=0.152)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.Button1 = tk.Button(self.TFrame1)
        self.Button1.place(relx=0.061, rely=0.242, height=29, width=139)
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''Play''')

        self.Button1_1 = tk.Button(self.TFrame1)
        self.Button1_1.place(relx=0.061, rely=0.485, height=29, width=139)
        self.Button1_1.configure(activebackground="#f9f9f9")
        self.Button1_1.configure(text='''Stop''')

        self.Button1_2 = tk.Button(self.TFrame1)
        self.Button1_2.place(relx=0.061, rely=0.727, height=29, width=139)
        self.Button1_2.configure(activebackground="#f9f9f9")
        self.Button1_2.configure(text='''Reset''')

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.061, rely=0.061, height=17, width=137)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(justify='center')
        self.TLabel2.configure(text='''Control''')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bg_color, fg=_fg_color, relief="flat")
        self.top.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="Game")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Load")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Save")
        self.sub_menu1 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="Help")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            command=self.show_about,
            foreground="#000000",
            label="About")

        self.TFrame2 = ttk.Frame(top)
        self.TFrame2.place(relx=0.009, rely=0.273, relheight=0.71, relwidth=0.152)
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame2)
        self.TLabel1.place(relx=0.061, rely=0.021, height=17, width=147)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text="Age")

        self.Canvas1 = grid_field.CanvasGrid(top, 60, 100, 10)
        self.Canvas1.place(relx=0.166, rely=0.01,
                           relheight=0.99, relwidth=0.9
                           )
        self.Canvas1.configure(borderwidth="2")
        # self.Canvas1.configure(relief="ridge")
        # self.Canvas1.configure(selectbackground="#c4c4c4")

    def show_about(self):
        window = tk.Toplevel(self.top)
        window.title("About")
        window.geometry("200x100")
        help_label = ttk.Label(window)
        help_label.configure(text='''This is Game of Life''')
        help_label.place(relx=0.061, rely=0.061)
