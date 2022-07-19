"""
Parent class for all windows.

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""

import tkinter as tk
from tkinter import ttk

def openReport():
    pass

def openHistory():
    pass

def openEntity():
    pass

def openBasis():
    pass

def openAlgorithm():
    pass

class Window(tk.Frame):
    menu_height = 52
    bg = 'blue'
    menu_bg = 'black'
    popup_bg = '#002244'
    body_bg = 'yellow'
    title = 'Report'


    def __init__ (self, master, *args, **kwargs):
        super().__init__(master, bg=self.bg, *args, **kwargs)
        titles = ['Report', 'Circuit', 'Archive', 'Truth Table', 'Basis', 'Algorithm']

        menubar = self.menubar = tk.Frame(self, bg=self.menu_bg, height=self.menu_height, relief='groove')
        self._windows_dropdown = tk.Frame(self, bg=self.popup_bg)
        title_var = self.title_var = tk.StringVar(menubar)
        self.opt = opt = ttk.OptionMenu(menubar, title_var, *titles, command=self.switch_window)
        opt.config(width=10)
        opt.grid(row=0, column=0, sticky='wns')
        
        
        menubar.rowconfigure(0, weight=1)
        body = self.body = tk.Frame(self, bg=self.body_bg, relief='groove')

            
        menubar.grid(row=0, column=0, sticky='wns')
        body.grid(row=1, column=0, sticky='wens')

        self.columnconfigure(0, weight=1)


        
    def openWindowsSelection(self):
        self._windows_dropdown.place(y=self.menu_height, relx=0)
        print('NaN button clicked!')

    def setup(self, windows):
        self.windows = windows

    def set_box(self, box):
        self.box = box

    def switch_window(self, *args):
        choise = self.title_var.get()
        fill = self.windows[choise]
        fill.title_var.set(choise)
        print(choise)
        fill.set_box(self.box)
        fill.box.forget(self)
        fill.box.add(fill)


class Circuit(Window):
    # bg ='#003636'
    title = 'Circuit'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)

class Archive(Window):
    title = 'Archive'
    bg = '#712F3E'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, bg=self.bg)
        self.title_var.set(self.title)
        self.config(width=500)
        self.menubar.config(width=500)
        self.body.config(width=500)

class TruthTable(Window):
    title = 'TruthTable'
    # bg = '#33bbff'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)

class Algorithm(Window):
    title = 'Algorithm'
    # bg = '#bd80ff'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)