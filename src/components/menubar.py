"""
Menu Bar

Author: Oleksii Dovhaniuk
Date: 15.06.2022
"""

import tkinter as tk
from tkinter import filedialog

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

def onAutoSave():
    pass

def onPreferences():
    pass

def onUndo():
    pass

def onRedo():
    pass

def onCut():
    pass

def onCopy():
    pass

def onPaste():
    pass

def openReport():
    pass

def openHistory():
    pass

def openEntity():
    pass

def openBasis():
    pass

def openAlgorithm():
    pass

def doFullScreen():
    pass

def onFind():
    pass

def doNothing():
    pass

def startAlgorithm():
    pass

def pauseAlgorithm():
    pass

def continueAlgorithm():
    pass

def stopAlgorithm():
    pass

def openGetStarted():
    pass

def openDocumentation():
    pass

def openAbout():
    pass


class MenuBar (tk.Menu):
    def __init__ (self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label='Open', command=onOpen, state='disabled', accelerator='Ctrl+O')
        file_menu.add_command(label='Save', command=onSave, state='disabled', accelerator='Ctrl+S')
        file_menu.add_command(label='Save As...', command=onSave, state='disabled', accelerator='Ctrl+Shift+S')
        file_menu.add_separator()
        file_menu.add_command(label='Auto Save', command=onAutoSave, state='disabled')
        file_menu.add_command(label='Preferences', command=onPreferences, state='disabled')
        file_menu.add_separator()

        file_menu.add_command(label='Quit', command=container.quit)
        self.add_cascade(label='File', menu=file_menu)

        edit_menu = tk.Menu(self, tearoff=0)
        edit_menu.add_command(label='Undo', command=onUndo, state='disabled', accelerator='Ctrl+Z')
        edit_menu.add_command(label='Redo', command=onRedo, state='disabled', accelerator='Ctrl+Shift+Z')
        edit_menu.add_separator()
        edit_menu.add_command(label='Cut', command=onCut, state='disabled', accelerator='Ctrl+X')
        edit_menu.add_command(label='Copy', command=onCopy, state='disabled', accelerator='Ctrl+C')
        edit_menu.add_command(label='Paste', command=onPaste, state='disabled', accelerator='Ctrl+V')
        edit_menu.add_separator()
        edit_menu.add_command(label='Find', command=onFind, state='disabled', accelerator='Ctrl+F')
        self.add_cascade(label='Edit', menu=edit_menu)

        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_command(label='Report', command=openReport, state='disabled', accelerator='Ctrl+Shift+R')
        view_menu.add_command(label='History', command=openHistory, state='disabled', accelerator='Ctrl+Shift+H')
        view_menu.add_command(label='Entity', command=openEntity, state='disabled', accelerator='Ctrl+Shift+E')
        view_menu.add_command(label='Basis', command=openBasis, state='disabled', accelerator='Ctrl+Shift+B')
        view_menu.add_command(label='Algorithm', command=openAlgorithm, state='disabled', accelerator='Ctrl+Shift+A')
        view_menu.add_separator()

        appearance_menu = tk.Menu(view_menu, tearoff=0)
        appearance_menu.add_command(label='Full Screen', command=doFullScreen, accelerator='F11')
        view_menu.add_cascade(label="Appearance", menu=appearance_menu, state='disabled')

        layout_editor_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label="Layout Editor", menu=layout_editor_menu, state='disabled')

        self.add_cascade(label='View', menu=view_menu)

        run_menu = tk.Menu(self, tearoff=0)
        run_menu.add_command(label='Start Algorithm', command=startAlgorithm, state='disabled', accelerator='F5')
        run_menu.add_command(label='Stop Algorithm', command=stopAlgorithm, state='disabled', accelerator='Shift+F5')
        run_menu.add_command(label='Restart Algorithm', command=stopAlgorithm, state='disabled', accelerator='Ctrl+Shift+F5')
        run_menu.add_separator()
        run_menu.add_command(label='Continue', command=continueAlgorithm, state='disabled', accelerator='F5')
        run_menu.add_command(label='Step', command=continueAlgorithm, state='disabled', accelerator='F10')
        self.add_cascade(label='Run', menu=run_menu)

        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label='Get Started', command=openGetStarted, state='disabled')
        help_menu.add_command(label='Documentation', command=openDocumentation, state='disabled')
        help_menu.add_separator()
        help_menu.add_command(label='About', command=openAbout, state='disabled')
        self.add_cascade(label='Help', menu=help_menu)



        container.config(menu=self)