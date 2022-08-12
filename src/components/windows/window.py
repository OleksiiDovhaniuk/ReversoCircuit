"""
Parent class for all windows.

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""

import tkinter as tk
from tkinter import ttk

# def openReport():
#     pass

# def openHistory():
#     pass

# def openEntity():
#     pass

# def openBasis():
#     pass

# def openAlgorithm():
#     pass

class Window(tk.Frame):
    """ A window for specified workflow. It is inherited from Tkinter Frame. It is a parent class for:
    windows.report.Report, 
    windows.circuit.Circuit, 
    windows.archive.Archive, 
    windows.truthTable.TruthTable, 
    windows.basis.Basis, 
    windows.algorithm.Algorithm.

    Constants
    ---------
    _titles : tuple
        A tuple of all windows titles (tuples of str). 

    Properties
    ----------
    title : str (default -> 'Report')
        A title of the window.
    bg : str
        Background color of the whole window.
    menubar : Tkinter Frame
        A local menubar.
    menu_bg : str
        Background color of window's menubar.
    popup_bg : str
        Background color of a drop down menu.
    menu_height : int
        Height of the window's menubar.
    body : Tkinter Frame
        A bulk part of the window.

    Methods
    -------
    switch_window : returns None
        Switches the current window to one from the _titles.
    """
    _titles = ('Report', 'Circuit', 'Archive', 'Truth Table', 'Basis', 'Algorithm')

    menu_height = 24
    bg = 'blue'
    menu_bg = '#F5F5F5'
    popup_bg = '#002244'
    body_bg = 'yellow'
    title = 'Report'


    def __init__ (self, master, *args, **kwargs):
        """ Initializes, configs and packs menubar and body of the window.
        """
        super().__init__(master, bg=self.bg, *args, **kwargs)

        # General menubar initialization and components
        self.menubar = menubar = tk.Frame(self, bg=self.menu_bg)
        menubar.pack(fill='x', side='top')

        self.left = left = tk.Frame(menubar)
        self.left.pack(side='left', fill='both')

        self.title_var = tk.StringVar(left)
        self.option_menu = ttk.OptionMenu(left, self.title_var, *self._titles, command=self.switch_window)
        self.option_menu.pack(side='left', fill='both')

        self.right = tk.Frame(menubar)
        self.right.pack(side='right', fill='both')

        # Body part of the Window initialization and components
        self.body = body = tk.Frame(self, bg=self.body_bg)
        body.pack(fill='both', side='bottom', expand=1)


    def switch_window(self, *args):
        """ Switches the current window to one from the _titles.
        """
        self.title_var.set(self.title)
        # choise = self.title_var.get()
        # fill = self.windows[choise]
        # fill.title_var.set(choise)
        # print(choise)
        # fill.set_box(self.box)
        # fill.box.forget(self)
        # fill.box.add(fill)


class Circuit(Window):
    """ The class represents a window for creating, editing and reviewing a circuits. Inherited from a Window class.
    """
    # bg ='#003636'
    title = 'Circuit'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)


class Algorithm(Window):
    """ The class represents a window for creating, editing and reviewing an algorithm. Inherited from a Window class.
    """
    title = 'Algorithm'
    # bg = '#bd80ff'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)