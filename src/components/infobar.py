"""
Bottom Infobar

Author: Oleksii Dovhaniuk
Date: 17.06.2022
"""
import tkinter as tk

VERSION = '0.0.0'

class Infobar(tk.Frame):
    bg = 'white'
    height = 32
    font_size = 8

    def __init__ (self, container, *args, **kwargs):
        super().__init__(container, bg=self.bg, height=self.height, highlightbackground='#E9E9E9', highlightthickness=1.5, *args, **kwargs)

        self.pack_propagate(0)

        version_lbl = tk.Label(self, text=VERSION, bg=self.bg, font=('Arial',self.font_size)) 
        version_lbl.pack(side='right')
        