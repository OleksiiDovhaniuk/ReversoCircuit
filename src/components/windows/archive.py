"""
Archive Windows.

Author: Oleksii Dovhaniuk
Date: 15.07.2022
"""

import tkinter as tk

from src.components.windows.window import Window

class Archive(Window):
    title = 'Archive'
    # bg = '#FFFFFF'
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)