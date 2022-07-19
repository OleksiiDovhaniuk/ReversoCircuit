"""
Bank part of the app's window.

Workspace can contain only window widgets of the app.

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""

import tkinter as tk
from src.components.windows.window import Circuit, Archive, TruthTable, Algorithm
from src.components.windows.basis import Basis
from src.components.windows.archive import Archive


class Workspace(tk.PanedWindow):
    _sashwidth = 4
    
    def __init__ (self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.right = right = tk.PanedWindow(self, sashrelief='raised', sashwidth=self._sashwidth, orient='vertical')
        top_right = Archive(right)
        bottom_right = Basis(right)
        self.left = left = tk.PanedWindow(self, sashrelief='raised', sashwidth=self._sashwidth, orient='vertical')
        top_left = TruthTable(left)
        top_left.body.config(width=1600)
        bottom_left = Circuit(left)

        top_right.config()
        bottom_right.config()


        self.add(left)
        self.add(right)
        right.add(top_right)
        right.add(bottom_right)
        right.sash_place(0, 1000, 1)
        left.add(top_left)
        left.add(bottom_left)


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
  

