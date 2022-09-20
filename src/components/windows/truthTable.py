"""
Basis windows.

Author: Oleksii Dovhaniuk
Date: 05.08.2022
"""

import tkinter as tk
import re

from src.components.windows.window import Window
from src.assets.common.table import ScrollableFrameXY


class EmptyCell(tk.Frame):
    """ A spaceholder with size of a cell. The class is inherited from a Tkinter Frame class.
    """
    pass

class TitleCell(tk.Entry):
    """ The first cell in a column. The class is inherited from a Tkinter Entry class.

    Arguments
    ---------
    _title : Tkinter StringVar
        Title of the input signal. Can be changed ith changing the cell text.

    Constants
    ---------
    WIDTH : int = 7
    STYPE : str = 'NaN'
        Signal type.
    """
    WIDTH = 7
    STYPE = 'NaN'

    def __init__(self, master, title, *args, **kwargs):
        self._title = tk.StringVar(master, title)
        self._invar = tk.StringVar(master, title)

        super().__init__(master, textvariable=self._invar, width=self.WIDTH, *args, **kwargs,
            # font=tk.font.Font(weight='bold'),
            )
        self.bind("<FocusOut>", self._onFocusOut)
    
    def _onFocusOut(self, event=None):
        """ Validate the signal title. Name should start from a letter, contains not more then 5 characters from a set [A-Za-z0-9_].
        If inputed string is epmty - call onEpmty().
        """
        value = self._invar.get()
        pattern = (
            r'^[A-Za-z][A-Za-z0-9_]{0}|'
            +r'^[A-Za-z][A-Za-z0-9_]{1}|'
            +r'^[A-Za-z][A-Za-z0-9_]{2}|'
            +r'^[A-Za-z][A-Za-z0-9_]{3}|'
            +r'^[A-Za-z][A-Za-z0-9_]{4}'
        )

        # if value == '':
        #     self._onEmpty()
        #     return

        if re.fullmatch(pattern, value):
            print('Haleluya')
            if self._pushTitleUpdate(self._title.get(), value, self.STYPE):
                self._title.set(value)
                return # if title is valid and not taken 

        if value == '':
            self._deleteLine(self._title.get(), self.STYPE)
            return # delete and return if the title is empty

        self._invar.set(self._title.get())

    def _onEmpty(self):
        """ Is called when the cell is empty.
        """
        print('Entry is empty.')

    def setOnEmpty(self, command):
        """ To set _onEmpty method from outside the class.

        Argumetns
        ---------
        command : def
            A function to implement on the empty cell.
        """
        pass
        # self._onEmpty = lambda 

    def setOnTitleUpdate(self, on_title_update, del_line):
        """ Sets the method which is called on title updates.
        """
        self._pushTitleUpdate = on_title_update
        self._deleteLine = del_line

class InputTitleCell(TitleCell):
    """ The first cell in a column. Title of an input signal. The class is inherited from a TitleCell class.

    Constants
    ---------
    BG : str = '#80D7F2'
        Background color of the cell.
    STYPE : str = 'in'
        Signal type.
    """
    BG = '#80D7F2'
    STYPE = 'in'

    def __init__(self, master, title, *args, **kwargs):
        super().__init__(master, title=title, bg=self.BG)

class OutputTitleCell(TitleCell):
    """ The first cell in a column. Title of an output signal. The class is inherited from a TitleCell class.

    Constants
    ---------
    BG : str = '#FF9900'
        Background color of the cell.
    STYPE : str = 'in'
        Signal type.
    """
    BG = '#FF9900'
    STYPE = 'out'

    def __init__(self, master, title, *args, **kwargs):
        super().__init__(master, title=title, bg=self.BG)

class IndexCell(tk.Label):
    """ The first cell in a row of values. The class is inherited from a Tkinter Label class.

    Arguments
    ---------
    index : Tkinter StringVar
        Index of the row.

    Constants
    ---------
    BG : str = '#F8F8F8'
        Background color of the cell.
    WIDTH : int = 3
        Width of the cell.
    """
    BG = '#B8B8B8'
    WIDTH = 3

    def __init__(self, master, index, *args, **kwargs):
        self.index = tk.StringVar(master, index)
        super().__init__(master, textvariable=self.index, bg=self.BG, width=self.WIDTH,
            # font=tk.font.Font(weight='bold'),
            )

class InputCell(tk.Label):
    """ An input value cell. The class is inherited from a Tkinter Label class.

    Arguments
    ---------
    value : Tkinter StringVar
        Signal value. One of {'0', '1'}.
    """

    def __init__(self, master, value, *args, **kwargs):
        self.value = tk.StringVar(master, value)
        super().__init__(master, textvariable=self.value) 

class OutputCell(tk.Button):
    """ An output value cell. The class is inherited from a Tkinter Button class.

    Constants
    ---------
    STATES : tuple = ('0', '1', 'X')

    Arguments
    ---------
    _state : Tkinter StringVar
        Signal value. One of {'0', '1', 'X'}.
    """
    STATES = ('0', '1', 'X')

    def __init__(self, master, state, *args, **kwargs):
        if state not in self.STATES:
            state = self.STATES[-1]

        self._state = tk.StringVar(master, state)
        super().__init__(master, textvariable=self._state, command=self._changeState)  

    def _changeState(self, *args, **kwargs):
        """ Changes the state of the cell to the next in an order {'0', '1', 'X'}.
        """
        next_index = (self.STATES.index(self._state.get()) + 1) % 3
        self._state.set(self.STATES[next_index])

    def setStateTrace(self, command):
        """ Set action no the cell, trigered by changing state variable.
        """
        self._state.trace_variable('w', lambda *_, v=self._state: command(v))


class Col:
    """ col of the Thruth Table.

    Atributes
    ---------
    _master : Tkinter Frame
        Body of the Truth Table.
    _index : int
        Number of the col.    
    _col : list 
        List of Cell objs.
    
    Methods
    -------
    creat(cells) returns : None
        Creates the col. Saves cell objs to _col list.

    show() returns : None
        Shows the col on the window.

    clear() returns : None
        Destroys all cells in the col. Clears _col list.
    """
    def __init__(self, master, cells, index=0, *args, **kwargs):
        """ Initialize _master and _col atributes.
        """
        self._master = master
        self._index = index 
        self.create(cells)

    def create(self, cells):
        """ Creates the col. returns List of Cell objs.

        Arguments
        ---------
        cells : nested list
            List view: [[<Cell Type>, <Cell Value>], ...]
        """
        self._col = col = []

        for i, [cell_type, value] in enumerate(cells):
            if cell_type == 'Empty':
                col.append(EmptyCell())
            elif cell_type == 'Title In':
                col.append(InputTitleCell(self._master, value))
            elif cell_type == 'Title Out':
                col.append(OutputTitleCell(self._master, value))
            elif cell_type == 'Index':
                col.append(IndexCell(self._master, i-1))
            elif cell_type == 'In':
                col.append(InputCell(self._master, value))
            elif cell_type == 'Out':
                col.append(OutputCell(self._master, value))

        return col


    def getTitle(self):
        """ Returns top cell of the column.
        """
        return self._col[0]

    def getValues(self):
        """ Returns all cells of the column except the title cell.
        """
        return self._col[1:]

    def show(self):
        """ Shows the column on the window.
        """
        self._col[0].grid(row=0, column=self._index, sticky='ns')
        for i, cell in enumerate(self._col[1:]):
            cell.grid(row=i+1, column=self._index, sticky='wens')

    def clear(self):
        """ Destroys all cells in the column. Clears _col list.
        """
        for cell in self._col:
            cell.destroy()
        self._col.clear()         



class TruthTable(Window):
    """ The class represents a window for creating, editing and reviewing a truth table. Inherited from a Window class.

    Atributes
    ---------
    _title : str
        A title of the window.
    _line_no : int
        Number of input or output signals.
    """
    title = 'TruthTable'

    _line_no = 3
    _data = {
        'in': {
            'X0': ['0', '0', '0', '0', '1', '1', '1', '1'],
            'X1': ['0', '0', '1', '1', '0', '0', '1', '1'],
            'X2': ['0', '1', '0', '1', '0', '1', '0', '1'],
        },
        'out': {
            'S':  ['0', '1', '1', '1', '1', '1', '1', '1'],
            'C':  ['0', '0', '0', '1', '0', '1', '1', '1'],
            'Y2': ['0', '1', '0', '1', '0', '1', '0', '1'],
        }
    }

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title_var.set(self.title)
        self._table = table = ScrollableFrameXY(self.body)

        self._addBtn = tk.Button(self.left, text='Add line', command=self.addLine)
        self._addBtn.pack(side='right', fill='both')
        self._check_btn = tk.Button(self.right, text='Check', state='disabled')
        self._check_btn.pack(side='right', fill='both')
        
        self._generate()
        self._show()

        table.pack(fill='both', expand=1)

    def _generate(self):
        """ Generates a truth table.
        """
        data = self._data
        body =  self._table.getBody()
        col_no = 0
        row_no = 2**self._line_no

        # Create an index column:
        indeces = [['Empty', None]]
        for i in range(row_no):
            indeces.append(['Index', None])
        self._cols = [Col(body, indeces)]
        col_no += 1
        
        # Create input signal columns:
        cols = [[['Title In', title]] for title in data['in']]
        for i, title in enumerate(data['in']):
            for value in data['in'][title]:
                cols[i].append(['In', value])
        for col in cols:
            new_col = Col(body, col, col_no)
            title_cell = new_col.getTitle()
            title_cell.setOnTitleUpdate(self.updateTitle, self.delLine)

            self._cols.append(new_col)
            col_no += 1

        # Create and add column-separator:
        vertical_separator = tk.Frame(body, bg='black')
        vertical_separator.grid(column=col_no, row=0, rowspan=row_no+1, sticky='ns')
        col_no += 1

        # Create output signal columns:
        cols = [[['Title Out', title]] for title in data['out']]
        for i, title in enumerate(data['out']):
            for value in data['out'][title]:
                cols[i].append(['Out', value])
        for col in cols:
            new_col = Col(body, col, col_no)
            title_cell = new_col.getTitle()
            title_cell.setOnTitleUpdate(self.updateTitle, self.delLine)

            self._cols.append(new_col)
            for index, cell in enumerate(new_col.getValues()):
                cell.setStateTrace(lambda v, s='out', t=title_cell.get(), i=index : self.updateValue(v, s, t, i))
            col_no += 1

    def _show(self):
        """ Show columns of the table.
        """
        for col in self._cols:
            col.show()

    def addLine(self, *args, **kwargs):
        """ Create and add new input and output signals to the table.

        Arguments
        ---------
        input : str
            Title of the input signal.
        output : str
            Title of the output signal.
        """
        row_no = 2**self._line_no

        # Inputs
        new_values = ['0' for _ in range(row_no)]
        new_values.extend(['1' for _ in range(row_no)])
        name_in = 'axl'
        keys_in = self._data['in'].keys()
        index = 1
        while f'{name_in}{index}' in keys_in:
            index += 1
        name_in += str(index)
            
        new_ins = {name_in : new_values}
        for title, values in self._data['in'].items():
            new_values = list(values)
            new_values.extend(list(values))
            new_ins[title] = new_values

        # Outputs
        new_values = ['0' for _ in range(row_no)]
        new_values.extend(['1' for _ in range(row_no)])
        name_out = 'grb'
        keys_out = self._data['out'].keys()
        index = 1
        while f'{name_out}{index}' in keys_out:
            index += 1
        name_out += str(index)

        new_outs = {name_out : ['X' for _ in range(row_no*2)]}
        for title, values in self._data['out'].items():
            new_values = list(values)
            new_values.extend(['X' for _ in range(row_no)])
            new_outs[title] = (new_values)

        self._data = {'in': new_ins, 'out': new_outs}
        self._line_no += 1

        # print(self._data, new_ins, new_outs)

        self.clearTable()
        self._generate()
        self._show()

    def delLine(self, title, stype):
        """Delete input and output signals from the table by their titles.

        Arguments
        ---------
        title : str
            Title of the signal.
        stype : str
            Signal's type. One of two {'in', 'out'}.
        """
        data = self._data

        if stype == 'in': 
            data['in'].pop(title)
            data['out'].pop()
        else:
            data['out'].pop(title)
            data['in'].popitem()

        if len(data[stype]) > 0:
            for sig_type in data:
                for title in data[sig_type]:
                    new_size = len(data[sig_type][title])//2
                    print(new_size)
                    new_values = data[sig_type][title][:new_size]
                    data[sig_type][title] = new_values

        self._line_no -= 1
        
        self.clearTable()
        self._generate()
        self._show()

    def clearTable(self):
        """ Clear all columns from the table.
        """
        for col in self._cols:
            col.clear()
            del col

    def updateTitle(self, old, new, stype):
        """ Updates a signal's title to the _data.

        Arguments
        ---------
        old : str
            Old title of the signal to be changed.
        new : str
            New title of the signal to which the title cell will be set.
        stype : str
            Signal's type. One of two {'in', 'out'}.
            
        Returns
        -------
        Boolean
            True if the title is updated, and False otherwise.
        """
        print(f'o={old}, n={new}, s={stype}')

        if new in self._data[stype]:
            print(f'{new} title is already occupied.')
            return False
        
        self._data[stype][new] = self._data[stype].pop(old)    
        print(self._data)
        return True

    def updateValue(self, var, stype, title, index):
        """ Updates a signal's value to the _data.

        Arguments
        ---------
        var : Tkinter StringVar
            Variable, which holds new value of the signal.
        stype : str
            Signal's type. One of two {'in', 'out'}.
        title : str
            Signal's title.
        index : int
            Order index of the value cell in a column (starting from 0).
        """
        self._data[stype][title][index] = var.get()
        # print(f'v={var.get()}, s={stype}, t={title}, i={index}')