"""
Reverso Circuit Lounching File

Author: Oleksii Dovhaniuk
Date: 14.06.2022
"""

import tkinter as tk
from tkinter import filedialog
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

class MainApp ():
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 3.0)
    root.geometry('1920x1080')
    root.iconbitmap("src/assets/icons/logo.ico")
    root.title('Reverso Circuit')
    # root.resizable(0, 0)



    workspace = Workspace(root)
    menubar = Menubar(root)
    infobar = Infobar(root)

    menubar.config()
    workspace.pack(fill='both', expand=1)
    infobar.pack(fill='both')


app = MainApp()
app.root.mainloop()