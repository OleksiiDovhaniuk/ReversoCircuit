"""
Bottom Infobar

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""
import tkinter as tk

VERSION = '0.3.0'

class Infobar(tk.Frame):
    bg = 'white'
    # font_size = 8

    def __init__ (self, container, height, *args, **kwargs):
        super().__init__(container, bg=self.bg, height=height, highlightbackground='#E9E9E9', highlightthickness=1.5, *args, **kwargs)
        self.height = height

        version_lbl = tk.Label(self, text=VERSION, bg=self.bg) 
        version_lbl.pack(side='right')
        