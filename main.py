"""
Reverso Circuit Lounching File

Author: Oleksii Dovhaniuk
Date: 14.06.2022
"""

import tkinter as tk
from tkinter import filedialog, font
import ctypes

from src.components.menubar import Menubar
from src.components.infobar import Infobar
from src.components.workspace import Workspace


ctypes.windll.shcore.SetProcessDpiAwareness(1)

def onOpen():
    print(filedialog.askopenfilename(
        initialdir = '/',
        title = 'Open file',
        filetypes = (('JSON files', '*.json'),),
    ))
    
def onSave():
    print(filedialog.asksaveasfilename(
        initialdir = '/',
        title = 'Save as',
        filetypes = (('JSON files', '.json'),),
    ))


class MainApp:

    def __init__(self, master: tk.Tk) -> None:
        self._zoom = _zoom = tk.IntVar(root, 1)
        _menubar_height = round(48*_zoom.get())
        _infobar_height = round(48*_zoom.get())
        _workspace_height = root.winfo_height() - _infobar_height

        workspace = Workspace(root, height=_workspace_height-_infobar_height)
        menubar = Menubar(root, height=_menubar_height)
        infobar = Infobar(root, height=_infobar_height)

        menubar.config()

        workspace.grid(row=0, column=0, sticky='wens')
        infobar.grid(row=1, column=0, sticky='wes')

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        


if __name__ == "__main__":
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 3.0)
    root.geometry('1920x1080')
    root.iconbitmap("src/assets/icons/logo.ico")
    root.title('Reverso Circuit')
  
    app = MainApp(root)
  
    # Mainloop to run application infinitely
    root.mainloop()