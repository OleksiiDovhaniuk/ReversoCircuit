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

class Window(tk.PanedWindow):
    menu_height = 52
    menu_bg = '#FFFFFF'
    popup_bg = '#002244'
    bg = '#DDDDDD'
    title = 'Report'


    def __init__ (self, container, *args, **kwargs):
        super().__init__(container, bg=self.bg, *args, **kwargs)
        # self._windows = {
        #     'Report': ['Ctrl+Shift+R', tk.PhotoImage(file='./src/assets/icons/icon_report.png')],
        #     'Archive': ['Ctrl+Shift+H', tk.PhotoImage(file='./src/assets/icons/icon_archive.png')],
        #     'Entity': ['Ctrl+Shift+E', tk.PhotoImage(file='./src/assets/icons/icon_entity.png')],
        #     'Basis': ['Ctrl+Shift+B', tk.PhotoImage(file='./src/assets/icons/icon_basis.png')],
        #     'Algorithm': ['Ctrl+Shift+A', tk.PhotoImage(file='./src/assets/icons/icon_algorithm.png')],
        #     }
        keys = ['Report', 'Report', 'Archive', 'Entity', 'Basis', 'Algorithm']

        menubar = tk.Frame(self, bg=self.menu_bg, height=self.menu_height, highlightbackground='#D9D9D9', relief='groove', highlightthickness=1.5)
        menubar.pack_propagate(0)
        
        # button = tk.Button(menubar, text='NaN',  relief='groove', width=80, command=self.openWindowsSelection)
        lbl = tk.Label(self, text="Hello, I'm here!", bg=self.bg)
        
        self._windows_dropdown = tk.Frame(self, bg=self.popup_bg)

        variable = self.variable = tk.StringVar(menubar)

        self.opt = opt = ttk.OptionMenu(menubar, variable, *keys, command=self.switch_window)
        opt.config(width=10, )
        opt.pack(side='left')
            
        menubar.pack(fill='both')
        # button.pack(side='left', fill='both')
        lbl.pack()
        
    def openWindowsSelection(self):
        self._windows_dropdown.place(y=self.menu_height, relx=0)
        print('NaN button clicked!')

    def setup(self, windows):
        self.windows = windows

    def switch_window(self, *args):
        self.pack_forget()
        choise = self.variable.get()
        print(choise)
        self.windows[choise].pack(fill='both', expand=1)
        self.windows[choise].variable.set(choise)


class Report(Window):
    bg ='#003636'
    title = 'Report'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable.set(self.title)

class Archive(Window):
    title = 'Archive'
    bg = '#712F3E'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable.set(self.title)

class Entity(Window):
    title = 'Entity'
    bg = '#33bbff'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable.set(self.title)

class Basis(Window):
    title = 'Basis'
    bg = '#ff5900'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable.set(self.title)

class Algorithm(Window):
    title = 'Algorithm'
    bg = '#bd80ff'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable.set(self.title)