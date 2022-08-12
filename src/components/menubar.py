"""
Menubar

Author: Oleksii Dovhaniuk
Date: 15.06.2022
"""

import tkinter as tk
from tkinter import filedialog, font
from PIL import Image, ImageTk

def onOpen():
    """Opens filedialoge window imported from the tkinter package in order to navigate and open a file.
    Because app data is going to be saved in json files, the filedialog will show only 
    .json files. 
    TODO: actually load file data.
    """
    print(filedialog.askopenfilename(
        initialdir = '/',
        title = 'Open file',
        filetypes = (('JSON files', '*.json'),),
    ))
    
def onSave():
    """ Opens filedialoge window imported from the tkinter package in order to navigate and save a file.
    Because app data is going to be saved in json files, the filedialog will show only 
    .json files. 
    TODO: actually save data to a file.
    """
    print(filedialog.asksaveasfilename(
        initialdir = '/',
        title = 'Save as',
        filetypes = (('JSON files', '.json'),),
    ))

def onAutoSave():
    """ Activates or deactivates auto save of the job.
    TODO: the method itself
    """
    pass

def onPreferences():
    """ Opens preferences window.
    TODO: the method itself
    """
    pass

def onUndo():
    """ Undo the last change, if possible.
    TODO: the method itself
    """
    pass

def onRedo():
    """ Redo the last change, if possible.
    TODO: the method itself
    """
    pass

def onCut():
    """ Cuts out selected text, if possible.
    TODO: the method itself
    """
    pass

def onCopy():
    """ Copies out selected text.
    TODO: the method itself
    """
    pass

def onPaste():
    """ Insertes copied or cut text into a focused entry.
    TODO: the method itself
    """
    pass

def openReport():
    """ Opens Report window, if still is not open one.
    TODO: the method itself
    """
    pass

def openArchive():
    """ Opens Archive window, if still is not open one.
    TODO: the method itself
    """
    pass

def openCircuit():
    """ Opens Circuit window, if still is not open one.
    TODO: the method itself
    """
    pass

def openBasis():
    """ Opens Basis window, if still is not open one.
    TODO: the method itself
    """
    pass

def openAlgorithm():
    """ Opens Algorithm window, if still is not open one.
    TODO: the method itself
    """
    pass

def openTruthTable():
    """ Opens Truth Table window, if still is not open one.
    TODO: the method itself
    """
    pass

def doFullScreen():
    """ Maximizes the program to a full screen.
    TODO: the method itself
    """
    pass

def onFind():
    """ Pops the find menu.
    TODO: the method itself
    """
    pass

def doNothing():
    """ Does as it seys.
    """
    pass

def startAlgorithm():
    """ Starts the job.
    TODO: the method itself
    """
    pass

def pauseAlgorithm():
    """ Pauses the job.
    TODO: the method itself
    """
    pass

def continueAlgorithm():
    """ Continue the paused job.
    TODO: the method itself
    """
    pass

def stopAlgorithm():
    """ Stops the job.
    TODO: the method itself
    """
    pass

def openGetStarted():
    """ Pops Get Started window up.
    TODO: the method itself
    """
    pass

def openDocumentation():
    """ Opens link in the default browser to program documentation.
    TODO: the method itself
    """
    pass

def openAbout():
    """ Pops About Us window up.
    TODO: the method itself
    """
    pass



class Menubar (tk.Menu):
    """ Menubar of the program. Inherited from Tkinter Menu. Consists of numerouse submenues to 
    manage the program.

    Parameters
    ----------
    master : MainApp
    height : int
        Height of the menubar.

    Methods
    -------
    config() : returns None
        Configs the menubar to the master.
    zoomIn() : returns None
        Magnifies displayed items.
    zoomOut() : returns None
        Reduces sizes of displayed items.
    zoomTo(value) : returns None
        Zooms to particular size of displayed items.
    zoomTo50() : returns None
        Reduces size of displayed items to 50% from default values.
    zoomTo100() : returns None
        Restores size of displayed items to 100%.
    zoomTo200() : returns None
        Magnifies displayed items in two times.
    """
    
    def zoomIn(self):
        """ Magnifies displayed items
        """
        for font_name in font.names():
            font_obj = font.nametofont(font_name)
            font_obj.configure(size=round(font_obj.cget('size')*1.25))

    def zoomOut(self):
        """ Reduces sizes of displayed items.
        """
        for font_name in font.names():
            font_obj = font.nametofont(font_name)
            font_obj.configure(size=round(font_obj.cget('size')*.8))
        

    def zoomTo(self, value):
        """ Zooms to particular size of displayed items.
        """
        for font_name in font.names():
            font_obj = font.nametofont(font_name)
            font_obj.configure(size=round(self._default_font_sizes[font_name]*value))

    def zoomToFit(self):
        """ Zoom to fit all blocks in Algorithm window.
        TODO: the method itself
        """
        pass

    def zoomTo50(self):
        """ Reduces size of displayed items to 50% from default values.
        """
        self.zoomTo(.5)

    def zoomTo100(self):
        """ Restores size of displayed items to 100%.
        """
        self.zoomTo(1)

    def zoomTo200(self):
        """ Magnifies displayed items in two times.
        """
        self.zoomTo(2)

    def __init__ (self, master, height, *args, **kwargs):
        """ Sets up properties of the class. Initializes, configures and add menues and submenues of the menubar."""
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.height = height
        self._default_font_sizes = {
            name: font.nametofont(name).cget('size') for name in font.names()
        }


        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label='Open', command=onOpen, state='disabled', accelerator='Ctrl+O')
        file_menu.add_command(label='Save', command=onSave, state='disabled', accelerator='Ctrl+S')
        file_menu.add_command(label='Save As...', command=onSave, state='disabled', accelerator='Ctrl+Shift+S')
        file_menu.add_separator()
        file_menu.add_command(label='Auto Save', command=onAutoSave, state='disabled')
        file_menu.add_command(label='Preferences', command=onPreferences, state='disabled')
        file_menu.add_separator()

        file_menu.add_command(label='Quit', command=master.quit)
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
        view_menu.add_command(label='Archive', command=openArchive, state='disabled', accelerator='Ctrl+Shift+H')
        view_menu.add_command(label='Circuit', command=openCircuit, state='disabled', accelerator='Ctrl+Shift+C')
        view_menu.add_command(label='Truth Table', command=openTruthTable, state='disabled', accelerator='Ctrl+Shift+T')
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

        zoom_menu = tk.Menu(self, tearoff=0)
        zoom_menu.add_command(label='Zoom in', command=self.zoomIn, accelerator='Ctrl++')
        zoom_menu.add_command(label='Zoom out', command=self.zoomOut, accelerator='Ctrl+-')
        # zoom_menu.add_command(label='Zoom to fit', command=self.zoomToFit, state='disabled', accelerator='Shift+1')
        zoom_menu.add_command(label='Zoom to 50%', command=self.zoomTo50)
        zoom_menu.add_command(label='Zoom to 100%', command=self.zoomTo100, accelerator='Shift+0')
        zoom_menu.add_command(label='Zoom to 200%', command=self.zoomTo200)
        self.add_cascade(label='Zoom', compound='right', menu=zoom_menu)


    def config(self):
        """ Sets up the master of the menubar as a menu."""
        self.master.config(menu=self)