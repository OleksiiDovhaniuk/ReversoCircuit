""" 
Table Common Components.

Author: Oleksii Dovhaniuk
Date: 15.07.2022
"""

import tkinter as tk


class ScrollableFrameXY(tk.Frame):
    """ A Tkinter Frame Obj which can be scrolled vertically and horizontaly
    
    Atributes
    ---------
    canvas : Tkinter Canvas
    scrollable_frame : Tkinter Frame
        An actual container for the widjets.
    canvas_frame : Tkinter Canvas Window

    Methods
    -------
    getBody(): return self.scrollable_frame
    """
    
    def __init__(self, master, *args, **kwargs):
        """Initialize canvas, scrollable_frame and canvas_frame. Configure canvas and canvas_frame.
        Packs canvas and scrollbar in the ScrollableFrameY.
        """
        super().__init__(master, *args, **kwargs)
        left_box =  tk.Frame(self)
        self.canvas = canvas = tk.Canvas(left_box)
        scrollbar_x = tk.Scrollbar(left_box, orient="horizontal", command=canvas.xview)
        scrollbar_y = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        self.canvas_frame = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        canvas.bind('<Configure>', self._upadateCanvasSize)

        left_box.pack(side="left", fill="both", expand=1)
        scrollbar_x.pack(side="bottom", fill="x")
        scrollbar_y.pack(side="right", fill="y")
        canvas.pack(side="top", fill="both", expand=1)

    def _upadateCanvasSize(self, event):
        """ Updates canvas size to the size of the event

        Parameters
        ----------
            event : event SEQUENCE
                Tkinter even SEQUENCE
        """
        pass
        # self.canvas.itemconfig(self.canvas_frame, width = event.width) 
        # self.canvas.itemconfig(self.canvas_frame, height = event.height) 

    def getBody(self): return self.scrollable_frame

class ScrollableFrameY(tk.Frame):
    """ A Tkinter Frame Obj which can be scrolled vertically
    
    Atributes
    ---------
    canvas : Tkinter Canvas
    scrollable_frame : Tkinter Frame
        An actual container for the widjets.
    canvas_frame : Tkinter Canvas Window
    """
    
    def __init__(self, master, *args, **kwargs):
        """Initialize canvas, scrollable_frame and canvas_frame. Configure canvas and canvas_frame.
        Packs canvas and scrollbar in the ScrollableFrameY.
        """
        super().__init__(master, *args, **kwargs)
        self.canvas = canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        self.canvas_frame = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', self._upadateWidthCanvas)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=1)

    def _upadateWidthCanvas(self, event):
        """ Updates canvas width to the width of the

        Parameters
        ----------
            event : event SEQUENCE
                Tkinter even SEQUENCE
        """
        self.canvas.itemconfig(self.canvas_frame, width = event.width) 

class Row(tk.Frame):
    """ A Tkinter Frame expanded in the table horizontaly.

    Parameters
    ----------
    bg : str
        A name of the background color such as 'white', 'black', 'blue', etc. or a hex code of the color.
    index : int
        An order number of the current row.
    placeholder : Tkinter Frame
        An empty Frame to make an empty row.
    empty_btn : Tkinter Button
        A disabled button with blankspace text ' ' packed in placeholder. Main usage of the button is to 
        make height of empty rows equal to the height of filled rows while zooming app widjets in or out.

    Methods
    -------
    fillPlaceholder() : returns None
        Creats a placeholder frame and packs empty_btn inside.
    clear() : returns None
        Destroys the placeholder (deletes the widget from the Row).
    """
    bg = 'white'
    placeholder = None
    empty_btn = None

    def __init__(self, master, bg=bg, index=' ', *args, **kwargs):
        """ Inherites constructor from Tkinter Frame class. Sets bg and index parameters.
        Calls fillPlaceholder module.
        """
        super().__init__(master, bg=bg, *args, **kwargs)
        self.bg = bg
        self.index= index

        self.fillPlaceholder()

    def fillPlaceholder(self):
        """ Creats a placeholder frame and packs empty_btn inside.
        """
        if self.placeholder: self.clear()
        
        self.placeholder = tk.Frame(self, bg=self.bg)
        self.placeholder.pack(fill='x', side='bottom')

        self.empty_btn = tk.Button(self.placeholder, text=f'{self.index}', bg=self.bg, relief='flat', state='disabled')
        self.empty_btn.pack(fill='both', expand=1)

    def clear(self):
        """ Destroys the placeholder (deletes the widget from the Row).
        """
        self.placeholder.destroy()

class Table(tk.Frame):
    """ A Tkinter Frame. The class represents a list table with objects as lines located in order 
    in the frame from top to bottom.

    Parameters
    ----------
    row_no : int
        A current number of rows.
    bg : str
        Background color of the table.
    bg_odd : str
        Background color of rows with odd index.
    rows : list
        A list of rows packed in the table.
    scrollable_frame : ScrollableFrameY obj
    box : Tkinter Frame
        A container for rows to pack.

    Methods
    -------
    deleteRow(row) : returns None
        Removes the row from rows list and destroys the row as a widget.
    addRow() : returns Row obj
        Creates a row with bg or bg_odd background, packs it in the table and returns it at the end.
    getBg(index) : returns str
        Returns the background color of the row with inputed index. If no index is given - gives the 
        background of the last row in the table.
    """
    row_no = 0
    bg = 'white'
    bg_odd = '#F0F0F0'

    def __init__(self, master, row_no=row_no, bg=bg, bg_odd=bg_odd, *args, **kwargs):
        """ Initialize rows, scrollable_frame and box. Packs scrollable_frame in a table.
        Creates and pack rows, if there are any.
        """
        super().__init__(master, bg=bg, *args, **kwargs)
        self.rows = []
        self.bg = bg
        self.bg_odd = bg_odd
        self.row_no = row_no

        self.scrollable_frame = ScrollableFrameY(self)
        self.box = box = self.scrollable_frame.scrollable_frame

        for i in range(row_no):
            if i % 2:
                row = Row(box, bg=bg)
            else:
                row = Row(box, bg=self.bg_odd)
            
            row.pack(fill='x')
            self.rows.append(row)
        
        self.scrollable_frame.pack(fill='both', expand=1)

    def deleteRow(self, row):
        """ Removes the row from rows list and destroys the row as a widget.

        Arguments
        ---------
        row : Row obj
        """
        self.rows.remove(row)
        row.destroy()


    def addRow(self, index):
        """ Creates a row with bg or bg_odd background, packs it in the table and returns it at the end.

        Returns
        -------
        Row obj
            A row from a rows at given index.
        """
        if len(self.rows) % 2:
            new_row = Row(self.box, bg=self.bg)
        else:
            new_row = Row(self.box, bg=self.bg_odd)
        new_row.pack(fill='x')
        self.rows.append(new_row)

        return self.rows[index]

    def getBg(self, index=None):
        """ Returns the background color of the row with inputed index. If no index is given - gives the 
        background of the last row in the table.

        Returns
        -------
        str
            A name of the background color such as 'white', 'black', 'blue', etc. or a hex code of the color.
        """
        if index == None:
            return self.rows[-1].bg
        else:
            return self.rows[index].bg