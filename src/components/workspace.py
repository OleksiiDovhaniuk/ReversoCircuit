"""
Bank part of the app's window.

Workspace can contain only window widgets of the app.

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""

import tkinter as tk
from src.components.windows.window import Circuit, TruthTable, Algorithm, Window
from src.components.windows.basis import Basis
from src.components.windows.archive import Archive


class Workspace(tk.PanedWindow):
    _sashwidth = 4
    _cat = [.15, .5, .75]
    
    def __init__ (self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.right = right = tk.PanedWindow(self, sashrelief='raised', sashwidth=self._sashwidth, orient='vertical')
        top_right = Archive(right)
        bottom_right = Basis(right)
        self.left = left = tk.PanedWindow(self, sashrelief='raised', sashwidth=self._sashwidth, orient='vertical')
        top_left = Window(left)
        bottom_left = Window(left)

        win_width = master.winfo_width()
        win_height = master.winfo_height()

        top_right.body.config(width=win_width*self._cat[0], height=win_height*self._cat[1])
        bottom_right.body.config(width=win_width*self._cat[0], height=win_height*(1-self._cat[1]))
        top_left.body.config(width=win_width*(1-self._cat[0]), height=win_height*self._cat[2])
        bottom_left.body.config(width=win_width*(1-self._cat[0]), height=win_height*(1-self._cat[2]))

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
  

