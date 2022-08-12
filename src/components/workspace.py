"""
Bank part of the app's window.

Workspace can contain only window widgets of the app.

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""

import tkinter as tk
from src.components.windows.window import Circuit, Algorithm, Window
from src.components.windows.basis import Basis
from src.components.windows.archive import Archive
from src.components.windows.truthTable import TruthTable


class Workspace(tk.PanedWindow):
    """ The main window of the program, inherited from Trkinter PanedWindow obj.
    
    Constants
    ---------
        _sashwidth : int
            Width of the paned windows sash
        _cut : list
            A list of floats represents ration in which windows accupy the workspace:
              first number shows relation right window to left window; 
              second number shows relation right-top window to right-bottom window; 
              third number shows relation left-top window to left-bottom window.

    Parameters
    ----------
        right: Tkinter PanedWindow obj
            Occupies whole right side of the workspace.
        left: Tkinter PanedWindow obj
            Occupies whole left side of the workspace.
        archive: Archive obj
            An archive window, where stores jobs of the program. Occupies right-top side of the workspace.
        basis: Basis obj
            A basis window. Manages basis elements of a circuit. Occupies right-bottom side of the workspace.
        truth_table: TruthTable obj
            A truth table window. Manages input and output signals of a circuit. 
            Occupies lefts-top side of the workspace.
    """
    _sashwidth = 4
    _cut = [.15, .5, .75]
    
    def __init__ (self, master, *args, **kwargs):
        """ Intializes,  configures and adds paned windows in the workspace.
        """
        super().__init__(master, *args, **kwargs)

        self.right = right = tk.PanedWindow(self, sashrelief='raised', sashwidth=self._sashwidth, orient='vertical')
        self.archive = top_right = Archive(right)
        self.basis = bottom_right = Basis(right)
        self.left = left = tk.PanedWindow(self, sashrelief='raised', sashwidth=self._sashwidth, orient='vertical')
        self.truth_table = top_left = TruthTable(left)
        bottom_left = Window(left)

        win_width = master.winfo_width()
        win_height = master.winfo_height()

        top_right.body.config(width=win_width*self._cut[0], height=win_height*self._cut[1])
        bottom_right.body.config(width=win_width*self._cut[0], height=win_height*(1-self._cut[1]))
        top_left.body.config(width=win_width*(1-self._cut[0]), height=win_height*self._cut[2])
        bottom_left.body.config(width=win_width*(1-self._cut[0]), height=win_height*(1-self._cut[2]))

        top_right.config()
        bottom_right.config()


        self.add(left, stretch="always")
        self.add(right,stretch="always")
        right.add(top_right, stretch="always")
        right.add(bottom_right, stretch="always")
        left.add(top_left, stretch="always")
        left.add(bottom_left, stretch="always")


        # master.bind("<Configure>", self.resize)

        # windows = self.windows ={
        #     'Report': Report(self, height=height, width=self.width*.5),
        #     'Archive': Archive(self, height=height*.5, width=self.width*.5),
        #     'Entity': Entity(self, height=height*.5, width=self.width*.5),
        #     'Basis': Basis(self, height=height, width=self.width*.5),
        #     'Algorithm': Algorithm(self, height=height, width=self.width*.5)
        # }

        # paned_wh.add(windows['Archive'])
        # paned_wv.add(windows['Basis'])
        # paned_wv.add(windows['Entity'])

        # for key in windows:
        #     windows[key].setup(windows)
        #     windows[key].pack_propagate(0)


        # windows['Basis'].pack(fill='both', side='top', expand=1)
        # windows['Archive'].pack(fill='both', side='left', expand=1)
        # windows['Entity'].pack(fill='both', side='bottom', expand=1)
  

