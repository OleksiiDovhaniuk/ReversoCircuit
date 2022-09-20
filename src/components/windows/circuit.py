"""
Circuit window.

Author: Oleksii Dovhaniuk
Date: 16.08.2022
"""

import tkinter as tk

from src.components.windows.window import Window
from src.components.cards.card import Card

from src.assets.common.table import ScrollableFrameXY


class InfoBoard(tk.Frame):
    """ Informational board with all specifications for a circuit. The class is inherited from Tkinter Frame.
    
    Parameters
    ----------
    line_no : int
        Number of lines in the circuit.
    qcost : int
        Quantum cost of the circuit.
    delay : int
        Delay of the circuit.
    abits : int
        Ancillary bits of the circuit.
    gbits : int
        Garbage bits of the circuit.
    parity : bool
        Parity preservation of the circuit.
    basis : list
        List of gates or elements used in circuit if form [[Gate, gate_number], ...].

    is_expand : bool
        If True the parameter's board is expant and it is collapsed otherwise.
    pos : list
        List of two elements [x, y], where x is a horizontal coordinte of the board and y is a vertical coordinate.

    Objects
    -------    
    _expand_btn : Tkinter Button
        Button to expand or collapse the board.
    _handle : Tkinter Button
        Button to move vertically the board in the circuit window.
    """
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        pass

class Signal(tk.Frame):
    """ Class which title of the Signal

    Parameters
    ----------
    _title : str
        Title of the signal.
    _direction : str
        Either 'in' or 'out'.
    """
    _title = 'NaN'
    _direction = 'in'

    def __init__(self, master, title=_title, direction=_direction):
        if direction in ('in', 'out'):
            self._direction = direction
        self._title = title

        pass

class DelBtn(tk.Button):
    """ Button to delete a gate from the circuit.
    """
    pass

class Cell(tk.Frame):
    """ A cell on the circuit line for a node of a gate.
    """
    pass

class Col(tk.Frame):
    """ General class for all columns in a circuit (signal column or a column for cells).
    """
    pass

class SignalCol(Col):
    """ A column class which contains only signal items.
    """
    pass

class GateCol(Col):
    """ A column that holds a place for a gate and DelBtn on the bottom of the column.
    """
    pass

class Gate:
    """ A class for a gate object to add, edit and remove from the circuit."""
    pass

class Circuit(Window):
    """ The class represents a window for creating, editing and reviewing a circuits. Inherited from a Window class.
    """
    title = 'Circuit'
    specs = [
        ['Label', 'Line No.', '0', 0],
        ['Label', 'Quantum Cost', '0', 0],
        ['Label', 'Delay', '0', 0],
        ['Label', 'Ancillary Bits', '0', 0],
        ['Label', 'Garbage Bits', '0', 0],
        ['Label', 'Parity', 'Preserved', 0],
        ['Label', 'Basis', '', 0],
        ['Label', 'GFRG - SWAP', '0', 1],
        ['Label', 'GFRG - CS', '0', 1],
    ]

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title_var.set(self.title)
        self._body = body = ScrollableFrameXY(self.body)

        specs_card = Card(body, self.specs, 'Specifications')

        body.pack(fill='both', expand=1)
        specs_card.place(anchor='ne', relx=.95, y=48)
