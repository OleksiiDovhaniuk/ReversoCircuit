"""
The file contains font settings.

Author: Oleksii Dovhaniuk
Date: 15.07.2022
"""

from tkinter import font

_default_font_sizes = {
    name: font.nametofont(name).cget('size') for name in font.names()
}
_scales = (.3, .35, .4, .45, .5, .62, .75, .87, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3)
pointer = 4
