"""
Bank part of the app's window.

Workspace can contain only window widgets of the app.

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""

import tkinter as tk
from src.components.windows.window import Report, Archive, Entity, Basis, Algorithm

class Workspace(tk.Frame):
    def __init__ (self, container, *args, **kwargs):
        super().__init__(container, relief='raised', *args, **kwargs)

        windows = {
            'Report': Report(self),
            'Archive': Archive(self),
            'Entity': Entity(self),
            'Basis': Basis(self),
            'Algorithm': Algorithm(self),
        }

        for key in windows:
            windows[key].setup(windows)

        windows['Archive'].pack(fill='both', expand=1)

