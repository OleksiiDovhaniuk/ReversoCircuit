"""
Reverso Circuit Lounching File

Author: Oleksii Dovhaniuk
Date: 14.06.2022
"""

import tkinter as tk
from tkinter import filedialog
import ctypes

from src.components.menubar import MenuBar

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
    root.resizable(0, 0)



    menubar = MenuBar(root)
    # filemenu = tk.Menu(menubar)
    # filemenu.add_command(label='Open', command=onOpen)
    # filemenu.add_command(label='Save', command=onSave)
    # filemenu.add_command(label='Quit', command=root.quit)
    # menubar.add_cascade(label='File', menu=filemenu)

    # root.config(menu=menubar)



app = MainApp()
app.root.mainloop()